import os
from transformers import AutoTokenizer, BertModel
from tokenize import tokenize, generate_tokens

tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased")
path = '/Users/haoye.tian/Documents/University/project/refactory/data/question_5/code/reference/reference.pure.py'

with open(path, 'rb') as f:
    text_tokens = tokenize(f.readline)
    print(sum(1 for dummy in text_tokens))