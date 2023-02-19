import json
import os
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, recall_score, precision_score
from basic_framework.core_testing import Tester
import ChatGPT as chatgpt
import Codex as codex
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
    chatgpt.ifbug(all_assignments, descriptions)

def program_repair(path, model):
    if model == 'ChatGPT':
        # chatgpt.repair(path)
        # chatgpt.validate(path)
        chatgpt.calculate()
    elif model == 'Codex':
        # codex.repair(path)
        # codex.validate(path)
        codex.calculate()


def code_explanation(path):

    chatgpt.explain(path)


if __name__ == '__main__':
    model = 'Codex'

    all_assignments, descriptions = load_data()
    # bug_detection(all_assignments, descriptions)

    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    program_repair(path, model)

    # code_explanation(path)


