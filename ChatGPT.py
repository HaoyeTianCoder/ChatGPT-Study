from chatgpt_wrapper import ChatGPT
import numpy as np
import openai
import os
import time
import signal
import json

from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, recall_score, precision_score
bot = ChatGPT()

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
# models = openai.Model.list()

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
    answer = bot.ask(prompt)
    return answer

def repair(path):
    fixed_id = json.load(open("fixed_id.json"))
    signal.signal(signal.SIGALRM, handler)
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
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
            # fixed_file_name = buggy_file_name.replace('wrong', 'fixed')
            # if os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
            #     continue
            id = assign.split('_')[2]
            fixed_file_name = buggy_file_name.replace('wrong', 'fixed3')
            if id in ids or os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
                continue

            path_wrong_assign = os.path.join(path_buggy_code, assign)
            buggy_version_code = open(path_wrong_assign).read().strip()
            # prompt = description + "\nGiven this task, is the following code correct? Answer me only with yes or no.\n\n " + assig_stu
            prompt = "There are bugs in one or more of the following codes, can you fix them? Reply me only with the fixed code. Do not include any natural language words, notes or explanations in your answer.\n\n " + buggy_version_code
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

                # remove natural language
                answer_list = answer.strip().split('\n')
                while not answer_list[0].startswith("def "):
                    answer_list.pop(0)
                # for i in range(len(answer_list)):
                #     if not answer_list[i].startswith('def '):
                #         answer_list.pop()
                #     else:
                #         break
                if answer_list[-1].startswith("```"):
                    answer_list.pop(-1)
                pure_code = '\n'.join(answer_list)

                with open(os.path.join(path_fixed_code, fixed_file_name), 'w+') as file:
                    file.write(pure_code)
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
            print('{}: {}'.format(cnt, buggy_file_name))
        response_time_average = np.array(response_time).mean()
        print('Response time average:')
        print('{}: {}'.format(q, response_time_average))


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
                # prompt = description + "\nGiven this task, is the following code correct? Answer me only with yes or no.\n\n " + assig_stu
                prompt = "Imagine you don't know the name of the function(s) below. Can you explain the intention of the function(s) within one sentence? Do not include any explanations of code details in your answer:\n\n " + code_content
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
            print('{}: {}'.format(q, response_time_average))