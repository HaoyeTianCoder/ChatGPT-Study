import numpy as np
import os
import openai
import time
import signal
import json
from main import *

openai.api_key = "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"


def repair(path):
    fixed_id = json.load(open("fixed_codex_id.json"))
    # signal.signal(signal.SIGALRM, handler)
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
        print(q)
        ids = fixed_id[q]
        cnt = 0
        response_time = []
        path_question = path + q
        path_fixed_code = os.path.join(path_question, 'code/fixed_codex')
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
            fixed_file_name = buggy_file_name.replace('wrong', 'fixed')
            if id in ids or os.path.exists(os.path.join(path_fixed_code, fixed_file_name)):
                continue

            path_wrong_assign = os.path.join(path_buggy_code, assign)
            buggy_version_code = open(path_wrong_assign).read().strip()
            prompt = "##### Fix bugs in the below function\n \n### Buggy Python\n" + buggy_version_code + "\n### Fixed Python"
            # prompt = "##### There are one or more bugs in the below code. Can you please fix them? Reply me only with the fixed code. Do not include any natural language words, notes or explanations in your answer.\n \n### Buggy Python\n" + buggy_version_code + "\n### Fixed Python"
            begin = time.time()
            # OpenAI API
            response = openai.Completion.create(
                model="code-davinci-002",
                prompt=prompt,
                # temperature=0,
                max_tokens=1024,
                # top_p=1.0,
                # frequency_penalty=0.0,
                # presence_penalty=0.0,
                stop=["###"]
            )

            answer = response.choices[0].text.strip().strip(',').strip('.')
            with open(os.path.join(path_fixed_code, fixed_file_name), 'w+') as file:
                file.write(answer)
            end = time.time()
            cost = end - begin
            if cost <= 5:
                time.sleep(5 - cost)
            print('{}: {}'.format(cnt, buggy_file_name))
        response_time_average = np.array(response_time).mean()
        print('Response time average:')
        print('{}: {}'.format(q, response_time_average))


def validate(path):
    all_result = []
    fixed_id = {}
    check = []
    for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
        print(q)
        fixed_id[q] = []
        question_path = path + q
        t = Tester(question_path)
        path_fixed_code = os.path.join(question_path, 'code/fixed_codex')
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
                    tr = t.tv_code(corr_code)
                except Exception as e:
                    print("{}: error!".format(file_name))
                    error += 1
                    check.append(file_name)
                    continue
                    # raise e
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
        # all_result.append([cnt, correct, wrong, error])
    print('lets check: {}'.format(sorted(check)))
    json.dump(fixed_id, open('fixed_codex_id.json', 'w+'))
    # print("cnt, correct, wrong, error")
    # print(all_result[0])
    # print(all_result[1])
    # print(all_result[2])
    # print(all_result[3])
    # print(all_result[4])



if __name__ == '__main__':

    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    # repair(path)
    validate(path)

