import json
import os
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc, accuracy_score, recall_score, precision_score
from basic_framework.core_testing import Tester
import ChatGPT as chatgpt
import Codex as codex
import word2vector as w2v
from basic_framework.refactoring import Refactoring, Reporter
from basic_framework.utils import regularize
from basic_framework.core_testing import Tester
from basic_framework.template import *
import pickle
from sklearn.metrics.pairwise import cosine_similarity

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

    # chatgpt.explain(path)

    # w2v.obtain_vectors(path)
    # run word2vector.py

    calculate_distribution()

def calculate_distribution():
    with open('./explanation_vectors.pickle', 'rb') as f:
        explanation_vectors = pickle.load(f)
    result = {}
    for k,v in explanation_vectors.items():
        print('question: {}'.format(k))
        result[k] = [[], []]
        correct_vectors = v['correct']
        print('correct:')
        for i in range(len(correct_vectors)):
            for j in range(i + 1, len(correct_vectors)):
                print('{} and {}'.format(correct_vectors[i][0], correct_vectors[j][0]))
                sim = cosine_similarity(correct_vectors[i][1].reshape(1, -1), correct_vectors[j][1].reshape(1, -1))
                result[k][0].append(sim[0][0])

        print('correct similarity: {}'.format(np.array(result[k][0]).mean()))
        wrong_vectors = v['wrong']
        print('wrong:')
        for i in range(len(wrong_vectors)):
            for j in range(i + 1, len(wrong_vectors)):
                print('{} and {}'.format(wrong_vectors[i][0], wrong_vectors[j][0]))
                sim = cosine_similarity(wrong_vectors[i][1].reshape(1, -1), wrong_vectors[j][1].reshape(1, -1))
                result[k][1].append(sim[0][0])
        print('wrong similarity: {}'.format(np.array(result[k][1]).mean()))

    print(result)


if __name__ == '__main__':
    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    model = 'Codex'

    # all_assignments, descriptions = load_data()
    # bug_detection(all_assignments, descriptions)

    # RQ-2
    # program_repair(path, model)

    #RQ-3
    code_explanation(path)


