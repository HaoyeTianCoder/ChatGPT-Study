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
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import pandas as pd
import seaborn as sns
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import scipy.stats as stats

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
        chatgpt.validate(path)
        chatgpt.calculate(path)
    elif model == 'Codex':
        # codex.repair(path)
        # codex.validate(path)
        codex.calculate()


def code_explanation(path):

    # chatgpt.explain(path)
    # chatgpt.explain_separated('./separation/')

    # w2v.obtain_vectors(path)
    # run word2vector.py

    # calculate_distribution()
    # calculate_distribution2()
    calculate_distribution3()

def calculate_distribution():
    with open('./explanation_vectors.pickle', 'rb') as f:
        explanation_vectors = pickle.load(f)
    result = []
    for k,v in explanation_vectors.items():
        print('question: {}'.format(k))
        correct_vectors = v['correct']
        print('correct:')
        for i in range(len(correct_vectors)):
            for j in range(i + 1, len(correct_vectors)):
                print('{} and {}'.format(correct_vectors[i][0], correct_vectors[j][0]))
                sim = cosine_similarity(correct_vectors[i][1].reshape(1, -1), correct_vectors[j][1].reshape(1, -1))
                result.append([k, 'Correct', sim[0][0]])

        # print('correct similarity: {}'.format(np.array(result[k][0]).mean()))
        wrong_vectors = v['wrong']
        print('wrong:')
        for i in range(len(wrong_vectors)):
            for j in range(i + 1, len(wrong_vectors)):
                print('{} and {}'.format(wrong_vectors[i][0], wrong_vectors[j][0]))
                sim = cosine_similarity(wrong_vectors[i][1].reshape(1, -1), wrong_vectors[j][1].reshape(1, -1))
                result.append([k, 'Incorrect', sim[0][0]])
        # print('wrong similarity: {}'.format(np.array(result[k][1]).mean()))

    # result = [[subject, group, value]]
    boxplot_distribution(result, 'Similarity of code intention',
                         'code_intention_similarity.jpg')

def calculate_distribution2():
    with open('./explanation_vectors.pickle', 'rb') as f:
        explanation_vectors = pickle.load(f)
    with open('./description_vectors.pickle', 'rb') as f:
        description_vectors = pickle.load(f)

    result = []
    for k,v in explanation_vectors.items():
        print('question: {}'.format(k))
        des_vector = description_vectors[int(k)-1]

        correct_vectors = v['correct']
        print('correct:')
        for i in range(len(correct_vectors)):
            sim = cosine_similarity(correct_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Correct', sim[0][0]])

        # print('correct similarity: {}'.format(np.array(result[k][0]).mean()))
        wrong_vectors = v['wrong']
        print('wrong:')
        for i in range(len(wrong_vectors)):
            sim = cosine_similarity(wrong_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Incorrect', sim[0][0]])
        # print('wrong similarity: {}'.format(np.array(result[k][1]).mean()))

    # result = [[subject, group, value]]
    boxplot_distribution(result, 'Similarity of code intention\n and question description',
                         'code_intention_similarity2.jpg')

def calculate_distribution3():
    with open('./separation_vectors.pickle', 'rb') as f:
        explanation_vectors = pickle.load(f)
    with open('./description_vectors.pickle', 'rb') as f:
        description_vectors = pickle.load(f)

    result = []
    for k,v in explanation_vectors.items():
        print('question: {}'.format(k))
        if k == 'unique_day':
            des_vector = description_vectors[5]
        elif k == 'unique_month':
            des_vector = description_vectors[6]
        elif k == 'contains_unique_day':
            des_vector = description_vectors[7]

        correct_vectors = v['correct']
        print('correct:')
        for i in range(len(correct_vectors)):
            sim = cosine_similarity(correct_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Correct', sim[0][0]])

        # print('correct similarity: {}'.format(np.array(result[k][0]).mean()))
        wrong_vectors = v['wrong']
        print('wrong:')
        for i in range(len(wrong_vectors)):
            sim = cosine_similarity(wrong_vectors[i][1].reshape(1, -1), des_vector.reshape(1, -1))
            result.append([k, 'Incorrect', sim[0][0]])
        # print('wrong similarity: {}'.format(np.array(result[k][1]).mean()))

    # result = [[subject, group, value]]
    boxplot_distribution(result, 'Similarity of code intention\n and question description',
                         'code_intention_similarity3.jpg')

def boxplot_distribution(distribution, y_title, figureName):
    dfl = pd.DataFrame(distribution)
    dfl.columns = ['Task', 'Group', y_title]
    # put H on left side in plot
    if dfl.iloc[0]['Group'] != 'Correct':
        b, c = dfl.iloc[0].copy(), dfl[dfl['Group']=='Correct'].iloc[0].copy()
        dfl.iloc[0], dfl[dfl['Group']=='Correct'].iloc[0] = c, b
    colors = {'Correct': 'white', 'Incorrect': 'grey'}
    fig = plt.figure(figsize=(15, 8))
    plt.xticks(fontsize=28, )
    plt.yticks(fontsize=28, )
    bp = sns.boxplot(x='Task', y=y_title, data=dfl, showfliers=False, palette=colors, hue='Group', width=0.7, notch=False)
    # bp.set_xticklabels(bp.get_xticklabels(), rotation=320)
    bp.set_xticklabels(bp.get_xticklabels())
    # bp.set_xticklabels(bp.get_xticklabels(), fontsize=28)
    # bp.set_yticklabels(bp.get_yticklabels(), fontsize=28)
    plt.xlabel('Task', size=32)
    plt.ylabel(y_title, size=30)
    plt.legend(fontsize=28, loc=1)
    # plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", borderaxespad=0, ncol=3, fontsize=30, )
    adjust_box_widths(fig, 0.8)
    # plt.tight_layout()
    plt.subplots_adjust(bottom=0.2, left=0.1)
    plt.savefig('./figure/' + figureName)
    print('The figure is saved to ./figure/' + figureName)
    plt.show()

    # distribution = np.array(distribution)
    # correct_list = []
    # distribution_c = distribution[np.array(distribution)[:, 1] == 'Correct']
    # for i in range(1, 11):
    #     mean_number = distribution_c[distribution_c[:, 0] == (str(i))][:,2].astype(int).mean()
    #     correct_list.append(mean_number)
    #
    # incorrect_list = []
    # distribution_inc = distribution[np.array(distribution)[:, 1] == 'Incorrect']
    # for i in range(1, 11):
    #     mean_number = distribution_inc[distribution_inc[:, 0] == (str(i))][:,2].astype(int).mean()
    #     incorrect_list.append(mean_number)

    # MWW test
    print()
    length_correct_list = dfl[dfl.iloc[:]['Group'] == 'Correct'][y_title].tolist()
    length_incorrect_list = dfl[dfl.iloc[:]['Group'] == 'Incorrect'][y_title].tolist()
    try:
        hypo = stats.mannwhitneyu(length_correct_list, length_incorrect_list, alternative='two-sided')
        # hypo = stats.mannwhitneyu(correct_list, incorrect_list, alternative='two-sided')
        p_value = hypo[1]
    except Exception as e:
        if 'identical' in e:
            p_value = 1
    print('p-value: {}'.format(p_value))
    if p_value <= 0.05:
        print('Reject Null Hypothesis: Significantly different!')
    else:
        print('Support Null Hypothesis!')

    # enumerate every questions
    question_list = sorted(set(dfl['Task'].tolist()))
    for q in question_list:
        print(q, end=': ')
        dfl_ques = dfl[dfl.iloc[:]['Task'] == q]
        length_correct_list = dfl_ques[dfl_ques.iloc[:]['Group'] == 'Correct'][y_title].tolist()
        length_incorrect_list = dfl_ques[dfl_ques.iloc[:]['Group'] == 'Incorrect'][y_title].tolist()
        try:
            hypo = stats.mannwhitneyu(length_correct_list, length_incorrect_list, alternative='two-sided')
            # hypo = stats.mannwhitneyu(correct_list, incorrect_list, alternative='two-sided')
            p_value = hypo[1]
        except Exception as e:
            if 'identical' in e:
                p_value = 1
        print('p-value: {}'.format(p_value))
        if p_value <= 0.05:
            print('Reject Null Hypothesis: Significantly different!')
        else:
            print('Support Null Hypothesis!')

def adjust_box_widths(g, fac):
    """
    Adjust the widths of a seaborn-generated boxplot.
    """
    # iterating through Axes instances
    for ax in g.axes:
        # iterating through axes artists:
        for c in ax.get_children():

            # searching for PathPatches
            if isinstance(c, PathPatch):
                # getting current width of box:
                p = c.get_path()
                verts = p.vertices
                verts_sub = verts[:-1]
                xmin = np.min(verts_sub[:, 0])
                xmax = np.max(verts_sub[:, 0])
                xmid = 0.5 * (xmin + xmax)
                xhalf = 0.5 * (xmax - xmin)

                # setting new width of box
                xmin_new = xmid - fac * xhalf
                xmax_new = xmid + fac * xhalf
                verts_sub[verts_sub[:, 0] == xmin, 0] = xmin_new
                verts_sub[verts_sub[:, 0] == xmax, 0] = xmax_new

                # setting new width of median line
                for l in ax.lines:
                    if np.all(l.get_xdata() == [xmin, xmax]):
                        l.set_xdata([xmin_new, xmax_new])


if __name__ == '__main__':
    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'

    # all_assignments, descriptions = load_data()
    # bug_detection(all_assignments, descriptions)

    # RQ-2
    program_repair(path, model='ChatGPT')

    #RQ-3
    # code_explanation(path)


