# In What Way is an LLM a Useful Assistant Bot for Programmers? An Empirical Study

An Empirical Study of ChatGPT
=======
We present an empirical study of ChatGPT's potential as a fully automated programming assistant, focusing on the tasks of code generation, program repair, and code summariziation.

## Ⅰ) Dataset
Zenodo Link: https://zenodo.org/record/7790888#.ZCfkuOwzZhE
  1. data: the responses produced by ChatGPT and Codex.
  2. data_des: the responses produced by ChatGPT_D and Codex_D.

## Ⅱ) Requirements
### A) Environment 
  * python 3.9 (Anaconda recommended)
  * pip install -r requirements.txt

## Ⅲ) Experiment

To obtain the experimental results of our paper, execute `run.py` with the following parameters:

### A) Sec. 4.1 (RQ-1: ChatGPT for Code Generation)

### A) Sec. 4.2 (RQ-2: ChatGPT for Program Repair)
Request ChatGPT to repair incorrect codes and save the responses in the folder **fixed**.
```
python main.py RQ2 repair ChatGPT
```
Validate the patched codes produced by ChatGPT.
```
python main.py RQ2 validate ChatGPT
```

### A) Sec. 4.3 (RQ-3: ChatGPT for Code Summarization)
Calculate similarity distributions in experiment 1.
```
python main.py RQ3 exp1
```
Calculate similarity distributions in experiment 2.
```
python main.py RQ3 exp2
```