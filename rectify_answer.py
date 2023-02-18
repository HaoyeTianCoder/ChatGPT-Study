import os

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
            if 'question_2' in root:
                continue
            if name.endswith(".py") and ('fixed_codex' in root.split('/')[-1]):
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

rectify_answer(top_dir)