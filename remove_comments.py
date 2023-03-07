#!/usr/bin/python
# -*- coding: <encoding name> -*-
import os
import re
import io
import sys, token, tokenize

# root path
top_dir = "/Users/haoye.tian/Documents/University/project/refactory/data"

# for folder
def trim_dir(path):
    check = []
    print("dir:" + path)
    for root, dirs, files in os.walk(path):
        # print("***")
        print(files)
        for name in files:
            if name.endswith(".py") and ("correct" or "wrong" in name):
            # if name.endswith(".py") and ('fixed' in root.split('/')[-1]):
                # trim_file(os.path.join(root,name))
                check += remove_comments_and_docstrings(root,name)
    print('###################')
    print('lets check: {}'.format(sorted(check)))

# for file
def trim_file(fname):
    """ Run on just one file.
    """
    source = open(fname)
    # mod = open(fname + ",strip", "w")
    mod = open(fname.replace(".py", ".pure.py"), "w")

    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0

    try:
        tokgen = tokenize.generate_tokens(source.readline)
        for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
            if 0:   # Change to if 1 to see the tokens fly by.
                print("%10s %-14s %-20r %r" % (
                    tokenize.tok_name.get(toktype, toktype),
                    "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                    ttext, ltext
                    ))
            if slineno > last_lineno:
                last_col = 0
            if scol > last_col:
                mod.write(" " * (scol - last_col))
            if toktype == token.STRING and prev_toktype == token.INDENT:
                # Docstring
                mod.write("#--")
            elif toktype == tokenize.COMMENT:
                # Comment
                mod.write("##\n")
            else:
                mod.write(ttext)
            prev_toktype = toktype
            last_col = ecol
            last_lineno = elineno
    except Exception as e:
        print("let's check: {}".format(fname))
        return

import io, tokenize, re
def remove_comments_and_docstrings(root,name):
    check = []
    path_file = os.path.join(root, name)
    with open(path_file, 'r') as f:
        source = f.read()
        io_obj = io.StringIO(source)
        out = ""
        prev_toktype = tokenize.INDENT
        last_lineno = -1
        last_col = 0
        try:
            for tok in tokenize.generate_tokens(io_obj.readline):
                token_type = tok[0]
                token_string = tok[1]
                start_line, start_col = tok[2]
                end_line, end_col = tok[3]
                ltext = tok[4]
                if start_line > last_lineno:
                    last_col = 0
                if start_col > last_col:
                    out += (" " * (start_col - last_col))
                if token_type == tokenize.COMMENT:
                    pass
                elif token_type == tokenize.STRING:
                    if prev_toktype != tokenize.INDENT:
                        if prev_toktype != tokenize.NEWLINE:
                            if start_col > 0:
                                out += token_string
                else:
                    out += token_string
                prev_toktype = token_type
                last_col = end_col
                last_lineno = end_line
            out = '\n'.join(l for l in out.splitlines() if l.strip())

            # return out
            # path_new_file = path_file.replace(".py", ".pure.py")
            path_new_file = path_file
            with open(path_new_file, 'w') as f:
                f.write(out)
        except Exception as e:
            check.append(name)
            return check
    # with open('test.py', 'r') as f:
    #     print(remove_comments_and_docstrings(f.read()))
    return check


import ast, astunparse
def remove_by_AST():
    with open('test.py') as f:
        lines = astunparse.unparse(ast.parse(f.read())).split('\n')
        for line in lines:
            if line.lstrip()[:1] not in ("'", '"'):
                print(line)

trim_dir(top_dir)