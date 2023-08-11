# ChatGPT as the Ultimate Programming Assistant: How Far Is It?

An Empirical Study of ChatGPT
=======
We present an empirical study of ChatGPT's potential as a fully automated programming assistant, focusing on the tasks of code generation, program repair, and code summariziation.

## Ⅰ) Dataset
Zenodo Link: https://zenodo.org/record/7792965#.ZCvyv-xBwUE
### A) LeetCode
1. Problems: code_generation_dataset/problems
2. Responses: code_generation_dataset/results
### B) Refactory
1. Submissions: data/.../code/(in)correct/
2. Responses:
   1. data/.../code/fixed(_codex)/: the responses of program repair produced by ChatGPT and Codex.
   2. data_des/.../code/fixed(_codex)/: the responses of program repair produced by ChatGPT_D and Codex_D.
   3. data/.../code/explanation/: the responses of code explanation produced by ChatGPT.

## Ⅱ) Requirements
### A) Environment 
  * python 3.9 (Anaconda recommended)
  * pip install -r requirements.txt

[//]: # (  * pip install git+https://github.com/mmabrouk/chatgpt-wrapper.git@v0.3.6)
[//]: # (Follow instructions on https://github.com/mmabrouk/chatgpt-wrapper/tree/v0.3.6 to setup ChatGPT web interface.)

### B) Configuration
  * update the absolute path of datasets in **config.py**.
  
## Ⅲ) Experiment
To obtain the experimental results of our paper, execute `main.py` with the following parameters:

### A) Sec. 4.1 (RQ-1: ChatGPT for Code Generation)
Request ChatGPT to generate codes and save the responses in the folder specified in `Config().generation_path`.
```
python main.py RQ1 generate ChatGPT
```
Print the Latex tables of submission results from ChatGPT, Codex, and CodeGen.
```
python main.py RQ1 table
```
Draw the boxplot of prompt lengths of correct and incorrect problems.
```
python main.py RQ1 length
```

### B) Sec. 4.2 (RQ-2: ChatGPT for Program Repair)
Request ChatGPT to repair incorrect codes and save the responses in the folder **fixed**.
```
python main.py RQ2 repair ChatGPT
```
Validate the patched codes produced by ChatGPT.
```
python main.py RQ2 validate ChatGPT
```
Perform Codex experiments by replacing ChatGPT with Codex. Evaluate ChatGPT_D and Codex_D by using 'data_des' instead of 'data' in `Config().path`.

### C) Sec. 4.3 (RQ-3: ChatGPT for Code Summarization)
Calculate similarity distributions in experiment 1.
```
python main.py RQ3 exp1
```

[//]: # (Calculate similarity distributions in experiment 2.)

[//]: # (```)

[//]: # (python main.py RQ3 exp2)

[//]: # (```)