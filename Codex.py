import numpy as np
import os
import openai
import time
import signal
import json

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
            # prompt = description + "\nGiven this task, is the following code correct? Answer me only with yes or no.\n\n " + assig_stu
            prompt = "##### Fix bugs in the below function\n \n### Buggy Python\n" + buggy_version_code + "\n### Fixed Python"
            begin = time.time()
            # OpenAI API
            response = openai.Completion.create(
                model="code-davinci-002",
                prompt=prompt,
                temperature=0,
                max_tokens=182,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )

            answer = response.choices[0].text.strip().strip(',').strip('.')
            with open(os.path.join(path_fixed_code, fixed_file_name), 'w+') as file:
                file.write(answer)
            end = time.time()
            cost = end - begin
            if cost <= 4:
                time.sleep(4 - cost)
            print('{}: {}'.format(cnt, buggy_file_name))
        response_time_average = np.array(response_time).mean()
        print('Response time average:')
        print('{}: {}'.format(q, response_time_average))

if __name__ == '__main__':

    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    repair(path)

