import os
import re

# root path
top_dir = "/Users/haoye.tian/Documents/University/project/refactory/data_nocomments"

# for folder
def rectify_answer(path):
    check = []
    print("dir:" + path)
    for root, dirs, files in os.walk(path):
        # print("***")
        print(files)
        for name in files:
            # if name.endswith(".py") and ("correct" or "wrong" in name):
            if name.endswith(".py") and ('fixed' in root.split('/')[-1]):
                if 'question_2' in root:
                # question_2 has 3 functions
                    rectify4question2(root, name)
                # if name.endswith(".py") and ('fixed_codex' in root.split('/')[-1]):
                else:
                    rectify(root, name)

def rectify(root, name):
    path_file = os.path.join(root, name)

    try:
        with open(path_file, 'r') as f:
            source = f.read()
        source_list = source.split('\n')
        while not source_list[0].startswith('def '):
            source_list.pop(0)
    except Exception as e:
        # print('')
        return
    patched_file = source_list[0] + '\n'
    for i in range(1, len(source_list)):
        if source_list[i].startswith('    '):
            patched_file += source_list[i] + '\n'
        else:
            break

    path_new_file = path_file
    with open(path_new_file, 'w') as f:
        f.write(patched_file)

def rectify4question2(root, name):
    path_file = os.path.join(root, name)
    patched_file = ''
    flag = False
    try:
        with open(path_file, 'r') as f:
            for line in f:
                if line.startswith('def '):
                    flag = True
                    patched_file += line
                elif flag and line.startswith('    '):
                    patched_file += line
                else:
                    flag = False
                    continue
    except Exception as e:
        print(e)

    path_new_file = path_file
    with open(path_new_file, 'w') as f:
        f.write(patched_file)

def rectify4question2_2(root, name):
    path_file = os.path.join(root, name)
    patched_file = ''
    for function_name in ['unique_day', 'unique_month', 'contains_unique_day']:
        try:
            function_code = extract(function_name, path_file)
        except Exception as e:
            # print(file)
            continue
        patched_file += function_code

    path_new_file = path_file
    with open(path_new_file, 'w') as f:
        f.write(patched_file)

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

rectify_answer(top_dir)
