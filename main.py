import json
import os
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, recall_score, precision_score
from basic_framework.core_testing import Tester
import ChatGPT as gpt
from basic_framework.refactoring import Refactoring, Reporter
from basic_framework.utils import regularize
from basic_framework.core_testing import Tester
from basic_framework.template import *

def load_data():
    data_path = '/Users/haoye.tian/Documents/University/project/refactory/data'
    questions = os.listdir(data_path)
    all_assignments = []
    descriptions = []
    for que in questions:
        que_path = os.path.join(data_path, que)
        description = open(os.path.join(que_path, 'description.txt')).read().strip()
        descriptions.append(description)
        ids = []
        assign_stus = []
        labels_stus = []

        # correct
        correct_assignment_path = os.path.join(que_path, 'code/correct/')
        files = os.listdir(correct_assignment_path)
        for f in files:
            if f.endswith('.py'):
                with open(os.path.join(correct_assignment_path, f), 'r+') as file:
                    assig_stu = file.read()
                ids.append(f)
                assign_stus.append(assig_stu)
                labels_stus.append(1)

        # wrong
        wrong_assignment_path = os.path.join(que_path, 'code/wrong/')
        files = os.listdir(wrong_assignment_path)
        for f in files:
            if f.endswith('.py'):
                with open(os.path.join(wrong_assignment_path, f), 'r+') as file:
                    assig_stu = file.read()
                ids.append(f)
                assign_stus.append(assig_stu)
                labels_stus.append(0)

        all_assignments.append([ids, assign_stus, labels_stus])
    return all_assignments, descriptions

def bug_detection(all_assignments, descriptions):
    gpt.ifbug(all_assignments, descriptions)

def program_repair(path):

    gpt.repair(path)

    validate(path)

def code_explanation(path):

    gpt.explain(path)

def validate(path):
    all_result = []
    fixed_id = {}
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
        # all_result.append([cnt, correct, wrong, error])

    json.dump(fixed_id, open('fixed_id.json', 'w+'))
    # print("cnt, correct, wrong, error")
    # print(all_result[0])
    # print(all_result[1])
    # print(all_result[2])
    # print(all_result[3])
    # print(all_result[4])


if __name__ == '__main__':
    # test correct programs

    all_assignments, descriptions = load_data()
    # bug_detection(all_assignments, descriptions)

    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    program_repair(path)

    # code_explanation(path)


