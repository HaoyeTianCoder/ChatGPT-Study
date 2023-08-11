import os
from transformers import AutoTokenizer, BertModel
import torch
import numpy
import json
import pickle

tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased")
model = BertModel.from_pretrained("bert-large-uncased")

def obtain_vectors(path):
    all = {'1': {'wrong':[], 'correct':[]},
           '2': {'wrong':[], 'correct':[]},
           '3': {'wrong':[], 'correct':[]},
           '4': {'wrong':[], 'correct':[]},
           '5': {'wrong':[], 'correct':[]}}
    cnt = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if root.split('/')[-1] == 'explanation' and file.startswith('explanation'):
                label = file.split('_')[1]
                question = file.split('_')[2]
                id = file.split('_')[3]
                code_intention = open(os.path.join(root, file), 'r+').read().strip()
                code_intention_vector = word2vector(code_intention)

                all[question][label].append([id, code_intention_vector])
                cnt += 1
                print('question-{}: {} {}'.format(question, cnt, id))

    with open('./explanation_vectors_API.pickle', 'wb') as f:
        pickle.dump(all, f)

def questions2vector():
    question1 = 'This function takes in a value “x” and a sorted sequence “seq”, and returns the position that “x” should go to such that the sequence remains sorted. Otherwise, return the length of the sequence.'
    question2 = 'Given a month and a list of possible birthdays, the functions check if there is only one possible birthday with that month and unique day.'
    question3 = 'This function takes in a list and returns a new list with all repeated occurrences of any element removed and the order of the original elements kept.'
    question4 = 'Given a list of people, this function sorts the people and returns a list in an order such that the older people are at the front of the list.'
    question5 = 'This function top_k accepts a list of integers as the input and returns the greatest k number of values as a list, with its elements sorted in descending order.'

    unique_day = 'This function checks whether a given day appears exactly once in the list of possible birthdays.'
    unique_month = 'This function checks whether a given month appears exactly once in the list of possible birthdays.'
    contains_unique_day = 'Given a month and a list of possible birthdays, returns True if there is only one possible birthday with that month and unique day, and False otherwise.'

    question1_vector = word2vector(question1)
    question2_vector = word2vector(question2)
    question3_vector = word2vector(question3)
    question4_vector = word2vector(question4)
    question5_vector = word2vector(question5)

    unique_day_vector = word2vector(unique_day)
    unique_month_vector = word2vector(unique_month)
    contains_unique_day_vector = word2vector(contains_unique_day)

    result = [question1_vector, question2_vector, question3_vector, question4_vector, question5_vector,
              unique_day_vector, unique_month_vector, contains_unique_day_vector]
    with open('./description_vectors.pickle', 'wb') as f:
        pickle.dump(result, f)

def obtain_vectors_separated(path):
    all = {'unique_day': {'wrong': [], 'correct': []},
           'unique_month': {'wrong': [], 'correct': []},
           'contains_unique_day': {'wrong': [], 'correct': []}}
    cnt = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if root.split('/')[-1] == 'explanation' and file.startswith('explanation'):
                label = file.split('_')[1]
                question = root.split('/')[-2]
                id = file.split('_')[3]
                code_intention = open(os.path.join(root, file), 'r+').read()
                code_intention_vector = word2vector(code_intention)

                all[question][label].append([id, code_intention_vector])
                cnt += 1
                print('question-{}: {} {}'.format(question, cnt, id))

    with open('./separation_vectors.pickle', 'wb') as f:
        pickle.dump(all, f)


def word2vector(text):

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)

    last_hidden_states = outputs.last_hidden_state

    # Compute the mean pooled embeddings
    mean_pooled = torch.mean(last_hidden_states, dim=1)

    # Compute the max pooled embeddings
    # max_pooled, _ = torch.max(last_hidden_states, dim=1)

    # Print the shape of the mean and max pooled embeddings
    # print("Mean embedding:", mean_pooled.detach().numpy())
    return mean_pooled.detach().numpy().flatten()

if __name__ == '__main__':
    path = '/Users/haoye.tian/Documents/University/project/refactory/data/'
    obtain_vectors(path)
    # questions2vector()
    # obtain_vectors_separated('./separation')
