from chatgpt_wrapper import ChatGPT
import numpy as np
import openai
import os
import time
import signal
import json
from main import *
from basic_framework.core_testing import Tester
bot = ChatGPT()

from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, recall_score, precision_score

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
# models = openai.Model.list()

# def __init__():
#     bot = ChatGPT()

def handler(signum, frame):
    raise Exception("time out")

def ifbug(all_assignments, descriptions):
    for i in range(len(descriptions)):
        labels_gpt = []
        des = descriptions[i]
        ids, assign_stus, labels_stus = all_assignments[i][0], all_assignments[i][1], all_assignments[i][2]
        answers_gpt = reque_chatgpt(des, ids, assign_stus, [], 0)
        for answer in answers_gpt:
            if answer.lower() == 'yes':
                labels_gpt.append(1)
            elif answer.lower() == 'no':
                labels_gpt.append(0)
            else:
                if 'yes' in answer.lower() and not 'no' in answer.lower():
                    labels_gpt.append(1)
                elif 'no' in answer.lower() and not 'yes' in answer.lower():
                    labels_gpt.append(0)
                else:
                    raise
        tn, fp, fn, tp = confusion_matrix(labels_stus, labels_gpt).ravel()
        acc = accuracy_score(y_true=labels_stus, y_pred=labels_gpt)
        prc = precision_score(y_true=labels_stus, y_pred=labels_gpt)
        re = '================\n'
        re += des + '\n'
        re += 'acc: {}, prc: {}\n'.format(acc, prc)
        re += 'tn  fp  fn  tp\n'
        re += '{}  {}  {}  {}\n'.format(tn, fp, fn, tp)
        print(re)
        with open('./result.txt', 'a+') as file:
            file.write(re)

def reque_chatgpt(description, ids, assign_stus, answers_gpt, i):
    try:
        while i < len(assign_stus):
            id = ids[i]
            assig_stu = assign_stus[i]
            # prompt = description + "\nGiven this task, is the following code correct? Answer me only with yes or no.\n " + assig_stu
            prompt = description + "\nGiven this task, do you find any bug in the following code? \n " + assig_stu
            begin = time.time()
            # OpenAI API
            # response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
            # answer = response.choices[0].text.strip().strip(',').strip('.')

            # ChatGPT API
            answer = bot.ask(prompt)
            response_time = time.time() - begin

            print('assignment: {}, review: {}'.format(id, answer))
            answers_gpt.append(answer)
            end = time.time()
            cost = end - begin
            if cost <= 2:
                time.sleep(2 - cost)

            i += 1

        if i >= len(assign_stus):
            return answers_gpt

    except Exception:
        time.sleep(10)
        return reque_chatgpt(description, ids, assign_stus, answers_gpt, i)

def ask(prompt):
    # bot = ChatGPT()
    answer = bot.ask(prompt)
    return answer

def repair(path, t):
    if not 'data_des' in path:
        if not os.path.exists("fixed_id.json"):
            json.dump({"question_1":[], "question_2":[], "question_3":[], "question_4":[], "question_5":[]}, open('fixed_id.json', 'w+'))
        fixed_id = json.load(open("fixed_id.json"))
    else:
        if not os.path.exists("fixed_id_des.json"):
            json.dump({"question_1":[], "question_2":[], "question_3":[], "question_4":[], "question_5":[]}, open('fixed_id_des.json', 'w+'))
        fixed_id = json.load(open("fixed_id_des.json"))
    # keep same with Codex
    descriptions = [
        'This function takes in a value “x” and a sorted sequence “seq”, and returns the position that “x” should go to such that the sequence remains sorted. Otherwise, return the length of the sequence.',
        'Given a month and a list of possible birthdays, these functions check if there is only one possible birthday with that month and unique day. Three different functions are implemented: unique_day, unique_month and contains_unique_day.',
        'This function takes in a list and returns a new list with all repeated occurrences of any element removed and the order of the original elements kept.',
        'Given a list of people, this function sorts the people and returns a list in an order such that the older people are at the front of the list.',
        'This function top_k accepts a list of integers as the input and returns the greatest k number of values as a list, with its elements sorted in descending order.']

    signal.signal(signal.SIGALRM, handler)
    questions = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']
    for i in range(len(questions)):
        q = questions[i]
        des = descriptions[i]
        print(q)

        ids = fixed_id[q]
        cnt = 0
        response_time = []
        path_question = path + q
        path_fixed_code = os.path.join(path_question, 'code/fixed')
        if not os.path.exists(path_fixed_code):
            os.makedirs(path_fixed_code)

        path_buggy_code = os.path.join(path_question, 'code/wrong')
        assignments_wrong = os.listdir(path_buggy_code)
        for assign in assignments_wrong:
            cnt += 1
            buggy_file_name = assign
            if buggy_file_name.startswith('.'):
                continue
            # fixed_file_name = buggy_file_name.replace('wrong', 'fixed')
            # if os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
            #     continue
            id = assign.split('_')[2]
            fixed_file_name = buggy_file_name.replace('wrong', 'fixed'+t) # enumerate fixed, fixed2, ..., fixed3
            # if id in ids or os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
            if os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
                continue

            path_wrong_assign = os.path.join(path_buggy_code, assign)
            buggy_version_code = open(path_wrong_assign).read().strip()
            # if q == 'question_2':
            #     # prompt = "There are one or more bugs in the below function(s). " + des + " Can you fix the function(s)? Reply to me with the three fixed functions. Do not include any natural language words, notes or explanations in your answer.\n\n " + buggy_version_code
            #     prompt = "There are one or more bugs in the below function(s). Can you fix the function(s)? Reply to me with the three fixed functions. Do not include any natural language words, notes or explanations in your answer.\n\n " + buggy_version_code
            # else:
            #     # prompt = "There are one or more bugs in the below function. " + des + " Can you fix the function? Reply to me with the fixed function. Do not include any natural language words, notes or explanations in your answer.\n\n " + buggy_version_code
            #     prompt = "There are one or more bugs in the below function. Can you fix the function? Reply to me with the fixed function. Do not include any natural language words, notes or explanations in your answer.\n\n " + buggy_version_code

            if q == 'question_2':
                prompt = "##### Fix bugs in the below functions\n" +des+ "\n### Buggy Python\n" + buggy_version_code + "\n### Fixed Python"
            else:
                prompt = "##### Fix bugs in the below function\n" +des+ "\n### Buggy Python\n" + buggy_version_code + "\n### Fixed Python"
            begin = time.time()
            signal.alarm(60*5)
            try:
                # # ChatGPT window
                # answer = bot.ask(prompt)
                # ChatGPT API
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}]
                )
                answer = completion.choices[0].message.content
                if answer == '':
                    raise Exception('null answer')
                elif 'ChatGPT' and 'unavailable' in answer:
                    raise Exception(answer)
                response_time.append(time.time() - begin)

                # remove natural language
                answer_list = answer.strip().split('\n')
                while not answer_list[0].startswith("def "):
                    answer_list.pop(0)
                pure_code = '\n'.join(answer_list)

                with open(os.path.join(path_fixed_code, fixed_file_name), 'w+') as file:
                    file.write(pure_code)
            except Exception as e:
                # raise
                signal.alarm(0)
                print(e.__str__())
                if 'ChatGPT' and 'unavailable' in e.__str__():
                    print('waiting 10 min to request again ...')
                    time.sleep(60*10)
                continue
            signal.alarm(0)
            end = time.time()
            cost = end - begin
            # if cost <= 2:
            #     time.sleep(2 - cost)
            print('{}: {}'.format(cnt, buggy_file_name))
        # response_time_average = np.array(response_time).mean()
        # print('Response time average:')
        # print('{}: {}'.format(q, response_time_average))


    # code = ''
    # response = openai.Completion.create(
    #     # model="code-davinci-002",
    #     model="text-davinci-002",
    #     prompt="##### Fix bugs in the below function\n \n### Buggy Python\n" + code + "\n### Fixed Python",
    #     temperature=0,
    #     max_tokens=182,
    #     top_p=1.0,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.0,
    #     stop=["###"]
    # )

def validate(path, metric):
    all_result = []
    fixed_id = {}
    all_id = {}
    check = []
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
        print(q)
        fixed_id[q] = []
        all_id[q] = []
        question_path = path + q
        t = Tester(question_path)
        path_fixed_code = os.path.join(question_path, 'code/fixed')
        assignments_fixed = os.listdir(path_fixed_code)
        cnt, correct, wrong, error = 0, 0, 0, 0
        for assign in assignments_fixed:
            if assign.startswith('.'):
                continue
            cnt += 1
            file_name = assign
            path_fixed_assign = os.path.join(path_fixed_code, assign)
            with open(path_fixed_assign, "r") as f:
                # file_name = path_fixed_assign.split("/")[-1]
                try:
                    corr_code = regularize(f.read())
                except Exception as e:
                    print("{}: error!".format(file_name))
                    check.append(file_name)
                    error += 1
                    continue
                    # raise e
                tr = t.tv_code(corr_code)
                assign_id = file_name.split('_')[2]
                if assign_id not in all_id[q]:
                    all_id[q].append(assign_id)
                if t.is_pass(tr):
                    # corr_code_map[file_name] = corr_code
                    print('{}: correct!'.format(file_name))
                    correct += 1
                    # q_id = file_name.split('_')[1]
                    if assign_id not in fixed_id[q]:
                        fixed_id[q].append(assign_id)
                else:
                    print('{}: incorrect!'.format(file_name))
                    wrong += 1
                    # print(tr)
                    # print(path_fixed_assign)
                    # shutil.move(corr_code_path, pseudo_corr_dir_path)
        all_result.append([cnt, correct, wrong, error, correct/cnt])

    # print(sorted(list(set(all_id['question_5']) - set(fixed_id['question_5']))))
    # print('lets check: {}'.format(sorted(check)))
    if not 'data_des' in path:
        json.dump(fixed_id, open('fixed_id.json', 'w+'))
    else:
        json.dump(fixed_id, open('fixed_id_des.json', 'w+'))

    # if metric == 'AVG5':
    print("AVG-5")
    print("cnt, correct, wrong, error, fix rate")
    print(all_result[0],)
    print(all_result[1])
    print(all_result[2])
    print(all_result[3])
    print(all_result[4])
    all_cnt = all_result[0][0] + all_result[1][0] + all_result[2][0] + all_result[3][0] + all_result[4][0]
    all_correctness = all_result[0][1] + all_result[1][1] + all_result[2][1] + all_result[3][1] + all_result[4][1]
    print('################')
    print('All: fix rate: {}'.format(all_correctness/all_cnt))

def validate_case(path):
    all_result = []
    fixed_id = {}
    check = []
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
        print(q)
        fixed_id[q] = []
        question_path = path + q
        t = Tester(question_path)
        path_fixed_code = os.path.join(question_path, 'code/fixed')
        assignments_fixed = os.listdir(path_fixed_code)
        cnt, correct, wrong, error = 0, 0, 0, 0
        for assign in assignments_fixed:
            if assign.startswith('.'):
                continue
            cnt += 1
            file_name = assign
            path_fixed_assign = os.path.join(path_fixed_code, assign)
            with open(path_fixed_assign, "r") as f:
                # file_name = path_fixed_assign.split("/")[-1]
                try:
                    corr_code = regularize(f.read())
                except Exception as e:
                    print("{}: error!".format(file_name))
                    check.append(file_name)
                    error += 1
                    continue
                    # raise e
                tr = t.tv_code(corr_code)
                if t.is_pass(tr):
                    # corr_code_map[file_name] = corr_code
                    print('{}: correct!'.format(file_name))
                    # q_id = file_name.split('_')[1]
                    assign_id = file_name.split('_')[2]
                    if assign_id not in fixed_id[q]:
                        fixed_id[q].append(assign_id)
                        correct += 1
                else:
                    print('{}: incorrect!'.format(file_name))
                    wrong += 1
                    # print(tr)
                    # print(path_fixed_assign)
                    # shutil.move(corr_code_path, pseudo_corr_dir_path)
    return fixed_id

def calculate(path):
    print('TOP-5')
    all_cnt = 1783
    fix_cnt = 0
    if not 'data_des' in path:
        with open('fixed_id.json', 'r+') as f:
            dict = json.load(f)
    else:
        with open('fixed_id_des.json', 'r+') as f:
            dict = json.load(f)
    for k, v in dict.items():
        fix_cnt_ques = len(set(v))
        fix_cnt += fix_cnt_ques
        if k == 'question_1':
            cnt = 575
        elif k == 'question_2':
            cnt = 435
        elif k == 'question_3':
            cnt = 308
        elif k == 'question_4':
            cnt = 357
        elif k == 'question_5':
            cnt = 108
        print('Question: {}, Fix :{}, Fix rate: {}'.format(k, fix_cnt_ques, round(fix_cnt_ques / cnt, 4)))
    print('################')
    print('All: fix_cnt: {}, fix_rate: {}'.format(fix_cnt, round(fix_cnt / all_cnt, 4)))

def explain(path):
    signal.signal(signal.SIGALRM, handler)
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
        print(q)
        cnt = 0
        response_time = []
        path_question = path + q
        path_code_explanation = os.path.join(path_question, 'code/explanation')
        if not os.path.exists(path_code_explanation):
            os.makedirs(path_code_explanation)

        for label in ['correct', 'wrong']:
            path_root_code = os.path.join(path_question, 'code/'+label)
            assignments = os.listdir(path_root_code)
            for assign in assignments:
                cnt += 1
                file_name = assign
                if file_name.startswith('.'):
                    continue
                explanation_file_name = 'explanation_' + file_name
                if os.path.exists(os.path.join(path_code_explanation, explanation_file_name)):
                    continue

                path_assign = os.path.join(path_root_code, assign)
                code_content = open(path_assign).read().strip()
                prompt = "Can you explain the intention of the below function(s) within one sentence? Do not include any explanations of code details in your answer:\n\n " + code_content
                # prompt = "Can you explain the intention of the below function(s) within one sentence? \n\n " + code_content
                begin = time.time()
                signal.alarm(60*5)
                try:
                    # # ChatGPT window
                    # answer = bot.ask(prompt)
                    # ChatGPT API
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": prompt}]
                    )
                    answer = completion.choices[0].message.content
                    if 'ChatGPT' and 'unavailable' in answer:
                        raise Exception(answer)
                    response_time.append(time.time() - begin)

                    with open(os.path.join(path_code_explanation, explanation_file_name), 'w+') as file:
                        file.write(answer)
                except Exception as e:
                    raise
                    signal.alarm(0)
                    print(e.__str__())
                    if 'ChatGPT' and 'unavailable' in e.__str__():
                        print('waiting 10 min to request again ...')
                        time.sleep(60*10)
                    continue
                signal.alarm(0)
                end = time.time()
                cost = end - begin
                # if cost <= 2:
                #     time.sleep(2 - cost)
                print('{}: {}'.format(cnt, file_name))
            response_time_average = np.array(response_time).mean()
            print('Response time average:')
            print('{}: {}'.format(q, response_time_average))

def explain_separated(path):
    signal.signal(signal.SIGALRM, handler)
    for f in ['unique_day', 'unique_month', 'contains_unique_day']:
        print(f)
        cnt = 0
        response_time = []
        path_function = path + f
        path_code_explanation = os.path.join(path_function, 'explanation')
        if not os.path.exists(path_code_explanation):
            os.makedirs(path_code_explanation)

        for label in ['correct', 'wrong']:
            path_root_code = os.path.join(path_function, label)
            assignments = os.listdir(path_root_code)
            for assign in assignments:
                cnt += 1
                file_name = assign
                if file_name.startswith('.'):
                    continue
                explanation_file_name = 'explanation_' + file_name
                if os.path.exists(os.path.join(path_code_explanation, explanation_file_name)):
                    continue

                path_assign = os.path.join(path_root_code, assign)
                code_content = open(path_assign).read().strip()
                # prompt = description + "\nGiven this task, is the following code correct? Answer me only with yes or no.\n\n " + assig_stu
                prompt = "Can you explain the original intention of the below function(s) within one sentence? Do not include any explanations of code details in your answer:\n\n " + code_content
                begin = time.time()
                # OpenAI API
                # response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
                # answer = response.choices[0].text.strip().strip(',').strip('.')
                signal.alarm(60*5)
                try:
                    # ChatGPT API
                    answer = bot.ask(prompt)
                    # answer = ask(prompt)
                    if 'ChatGPT' and 'unavailable' in answer:
                        raise Exception(answer)
                    response_time.append(time.time() - begin)

                    with open(os.path.join(path_code_explanation, explanation_file_name), 'w+') as file:
                        file.write(answer)
                except Exception as e:
                    raise
                    signal.alarm(0)
                    print(e.__str__())
                    if 'ChatGPT' and 'unavailable' in e.__str__():
                        print('waiting 10 min to request again ...')
                        time.sleep(60*10)
                    continue
                signal.alarm(0)
                end = time.time()
                cost = end - begin
                if cost <= 2:
                    time.sleep(2 - cost)
                print('{}: {}'.format(cnt, file_name))
            response_time_average = np.array(response_time).mean()
            print('Response time average:')
            print('{}: {}'.format(f, response_time_average))
