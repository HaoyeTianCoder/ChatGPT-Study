import os
from transformers import AutoTokenizer, BertModel
import torch
import numpy
import json

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
                code_intention = open(os.path.join(root, file), 'r+').read()
                code_intention_vector = word2vector(code_intention)

                all[question][label].append([id, code_intention_vector])
                cnt += 1
                print('question-{}: {} {}'.format(question, cnt, id))
                if cnt == 101:
                    break

    with open('./explanation_vectors.json', 'w+') as f:
        json.dump(all, f)

def word2vector(text):
    tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased")
    model = BertModel.from_pretrained("bert-large-uncased")

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
    path = '/Users/haoye.tian/Documents/University/project/refactory/data_nocomments/'
    obtain_vectors(path)

    text = 'hello world!'
    word2vector(text)
