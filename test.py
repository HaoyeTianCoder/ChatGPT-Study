import os
import shutil
import ChatGPT as chatgpt

path = '/Users/haoye.tian/Documents/University/project/refactory/data/'
path2 = '/Users/haoye.tian/Documents/University/project/refactory/data_des/'
fixed = chatgpt.validate_case(path)
fixed2 = chatgpt.validate_case(path2)

for q in ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']:
    print(q)
    reduce = set(fixed[q]) - set(fixed2[q])
    increase = set(fixed2[q]) - set(fixed[q])
    print('reduce: {}'.format(list(reduce)))
    print('increase: {}'.format(list(increase)))