import os
import re

def extract(function_name, path_code):
    # Define the function name you want to extract
    # function_name = "contains_unique_day"

    # Open the source file and read its contents
    with open(path_code, "r") as source_file:
        source_code = source_file.read()

    # Use regular expressions to find the function definition
    pattern = r"def\s+" + function_name + r"\s*\(.*?\)\s*:\n(?:\s*#.*)*([\s\S]*?)(?=\n\s*def|\Z)"
    match = re.search(pattern, source_code)
    if not match:
        raise ValueError(f"Function '{function_name}' not found in source code")

    # Write the function code to a new file
    function_code = match.group(0)

    return function_code
    # with open(f"{function_name}.py", "w") as function_file:
    #     function_file.write(function_code)

def iterate(path_question2):
    path_correct = os.path.join(path_question2, 'correct')
    for root, dirs, files in os.walk(path_correct):
        for file in files:
            path_code = os.path.join(root, file)
            for function_name in ['unique_day', 'unique_month', 'contains_unique_day']:
                function_code = extract(function_name, path_code)
                new_path = './separation/'+function_name+'/correct'
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                with open(os.path.join(new_path, file), "w") as function_file:
                    function_file.write(function_code)

    path_incorrect = os.path.join(path_question2, 'wrong')
    for root, dirs, files in os.walk(path_incorrect):
        for file in files:
            path_code = os.path.join(root, file)
            for function_name in ['unique_day', 'unique_month', 'contains_unique_day']:
                try:
                    function_code = extract(function_name, path_code)
                except Exception as e:
                    # print(file)
                    continue
                new_path = './separation/'+function_name+'/wrong'
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                with open(os.path.join(new_path, file), "w") as function_file:
                    function_file.write(function_code)

def count(path_question2):
    cnt = 0
    path_fixed = os.path.join(path_question2, 'fixed')
    for root, dirs, files in os.walk(path_fixed):
        for file in files:
            path_code = os.path.join(root, file)
            for function_name in ['unique_day', 'unique_month', 'contains_unique_day']:
                try:
                    function_code = extract(function_name, path_code)
                except Exception as e:
                    print(file)
                    continue
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    path_question2 = '/Users/haoye.tian/Documents/University/project/refactory/data/question_2/code/'
    # iterate(path_question2)

    count(path_question2)