import subprocess, glob, os, time, random
from config import Config
from tqdm import tqdm

class LeetCodeUtil:
    def __init__(self):
        pass
    
    def generate_submit_file(self, output_file, model_name):
        
        if model_name=='ChatGPT':
            def remove_import(ans:str)->str:
                ans_arr=ans.split('\n')
                for i, l in enumerate(ans_arr):
                    if l.startswith('import ') or l.startswith('from ') or l.strip()=='':
                        continue
                    else:
                        return '\n'.join(ans_arr[i:])
                return ''
            def remove_line_comment(code:str):
                return '\n'.join([l for l in code.split('\n') if not l.strip().startswith('#')])
            with open(output_file,'r',encoding='UTF8') as f:
                problem_id=os.path.basename(os.path.dirname(os.path.dirname(output_file))).split('-')[0]
                test_num=os.path.basename(output_file).split('_')[-1].split('.')[0]
                ans=f.read().strip()
                ans=remove_line_comment(ans)
                ans=ans.replace("```python","```")
                if ans.startswith("```") and ans.endswith("```"): ans=ans[3:-3].strip()
                ans_splits=ans.split("```")
                class_splits=[l.strip() for l in ans_splits if remove_import(l.strip()).startswith('class ')]
                class_splits.sort(key=lambda x:len(x.split('\n')))
                ans=class_splits[-1]
                assert(remove_import(ans).startswith('class '))
                ans=f'# @lc app=leetcode id={problem_id} lang=python3\n'+ans
                py_file_path=os.path.join(os.path.dirname(output_file),f'{problem_id}.output_{test_num}.py')
                assert("class " in [l for l in remove_import(remove_line_comment(ans)).split('\n') if l.strip()!=''][0])
                try: assert("return" in ans)
                except: print('return not found:',output_file)
                with open(py_file_path,'w',encoding='UTF8') as fw:
                    fw.write(ans)
                print('Generated',py_file_path)
                
        elif model_name=='Codex':
            def remove_block_comment(code:str):
                code=''.join(code.split("'''")[::2])
                code=''.join(code.split('"""')[::2])
                return code
            def remove_line_comment(code:str):
                return '\n'.join([l for l in code.split('\n') if not l.strip().startswith('#')])
            def remove_empty_line(code:str):
                return '\n'.join([l for l in code.split('\n') if l.strip()!=''])
            # assume remove_block_comment, remove_line_comment, and remove_empty_line are called before
            def extract_imports(code:str):
                '''extract import statements from code'''
                code_arr=code.split('\n')
                import_lines=[]
                for l in code_arr:
                    if l.startswith('import') or l.startswith('from'):
                        import_lines.append(l)
                    else: break
                imports, code='\n'.join(import_lines), '\n'.join(code_arr[len(import_lines):])
                return imports, code
            def remove_code_before(code:str, start:str):
                '''remove code before start'''
                code_arr=code.split('\n')
                for i, l in enumerate(code_arr):
                    if l.startswith(start):
                        code='\n'.join(code_arr[i:])
                        break
                return code

            with open(output_file,'r',encoding='UTF8') as f:
                problem_id=os.path.basename(os.path.dirname(os.path.dirname(output_file))).split('-')[0]
                test_num=os.path.basename(output_file).split('_')[-1].split('.')[0]
                ans=f.read()
                ans=remove_empty_line(remove_line_comment(remove_block_comment(ans)))
                imports,ans=extract_imports(ans)
                try: assert(ans.startswith('class '))
                except: 
                    print(f'Ans does not start with class Solution: {output_file}')
                    ans=remove_code_before(ans, 'class ')
                    print(ans)
                ans_arr=ans.split('\n')
                try: assert(ans_arr[1].startswith('    '))
                except: print(f'Indentation format is not 4 spaces: {output_file}')
                temp=[]
                for l in ans_arr[1:]:
                    if l.startswith('    ') or l.startswith('\t'): temp.append(l)
                    else:  break
                ans_arr=[ans_arr[0],]+temp
                ans=imports+'\n'+'\n'.join(ans_arr)
                ans=f'# @lc app=leetcode id={problem_id} lang=python3\n'+ans
                py_file_path=os.path.join(os.path.dirname(output_file),f'{problem_id}.output_{test_num}.py')
                with open(py_file_path,'w',encoding='UTF8') as fw:
                    fw.write(ans)
                print('Generated',py_file_path)

        elif model_name=='CodeGen':
            def remove_block_comment(code:str):
                code=''.join(code.split("'''")[::2])
                code=''.join(code.split('"""')[::2])
                return code
            def remove_line_comment(code:str):
                return '\n'.join([l for l in code.split('\n') if not l.strip().startswith('#')])
            def remove_empty_line(code:str):
                return '\n'.join([l for l in code.split('\n') if l.strip()!=''])
            # assume remove_block_comment, remove_line_comment, and remove_empty_line are called before
            def extract_imports(code:str):
                '''extract import statements from code'''
                code_arr=code.split('\n')
                import_lines=[]
                for l in code_arr:
                    if l.startswith('import') or l.startswith('from'):
                        import_lines.append(l)
                    else: break
                imports, code='\n'.join(import_lines), '\n'.join(code_arr[len(import_lines):])
                return imports, code
            def remove_code_before(code:str, start:str):
                '''remove code before start'''
                code_arr=code.split('\n')
                for i, l in enumerate(code_arr):
                    if l.startswith(start):
                        code='\n'.join(code_arr[i:])
                        break
                return code
            
            with open(output_file,'r',encoding='UTF8') as f:
                problem_id=os.path.basename(os.path.dirname(os.path.dirname(output_file))).split('-')[0]
                test_num=os.path.basename(output_file).split('_')[-1].split('.')[0]
                ans=f.read()
                ans=remove_empty_line(remove_line_comment(remove_block_comment(ans)))
                imports,ans=extract_imports(ans)
                try: assert(ans.startswith('class '))
                except: 
                    print(f'Ans does not start with class Solution: {output_file}')
                    ans=remove_code_before(ans, 'class ')
                    print(ans)
                ans_arr=ans.split('\n')
                try: assert(ans_arr[1].startswith('    '))
                except: print(f'Indentation format is not 4 spaces: {output_file}')
                temp=[]
                for l in ans_arr[1:]:
                    if l.startswith('    ') or l.startswith('\t'): temp.append(l)
                    else:  break
                ans_arr=[ans_arr[0],]+temp
                ans=imports+'\n'+'\n'.join(ans_arr)
                ans=f'# @lc app=leetcode id={problem_id} lang=python3\n'+ans
                ans=ans.replace('<|endoftext|>','')
                py_file_path=os.path.join(os.path.dirname(output_file),f'{problem_id}.output_{test_num}.py')
                with open(py_file_path,'w',encoding='UTF8') as fw:
                    fw.write(ans)
                print('Generated',py_file_path)
        
        else: assert(False, f'Unknown model_name: {model_name}')
        
        return py_file_path
    
    def remove_leetcode_result(self, py_file_path):
        result_path=py_file_path.replace('.py','_result.txt')
        if os.path.exists(result_path): os.remove(result_path)
        
    def run_leetcode_test(self, model_name):
        config=Config()
        root_path=os.path.normpath(config.generation_path)
        py_files=glob.glob(root_path+'/results/'+model_name+'/**/*output_*.py',recursive=True)
        def result_exists(result_file:str):
            if not os.path.exists(result_file): return False
            with open(result_file,'r',encoding='UTF8') as f:
                result=f.read()
            if "[ERROR] Problem not found!" in result or "ECONNRESET" in result \
                or "Error: socket hang up" in result or "Error: connect ETIMEDOUT" in result \
                    or "Error: getaddrinfo ENOTFOUND" in result or "ECONNABORTED" in result \
                        or "[ERROR] Error: write EPROTO " in result: return False
            return True

        error_exists=True
        error_cnt=0
        error_total=0
        prev_err=False
        while(error_exists):
            error_exists=False
            error_cnt=0
            error_total=0
            iter_list=[p for p in py_files if not result_exists(p[:-3]+'_result.txt')]
            for py_file in tqdm(iter_list):
                py_result_file=py_file[:-3]+'_result.txt'
                p=subprocess.run(['leetcode-cli','submit',py_file,'-l','python3'],capture_output=True)
                if 'http error' in str(p.stdout) or "[ERROR] session expired" in str(p.stdout) or\
                    "[ERROR] Problem not found!" in str(p.stdout): 
                    error_exists=True
                    error_total+=1
                    if prev_err: error_cnt+=1
                    else: error_cnt=1
                    prev_err=True
                    if error_cnt>20: 
                        print('Too many errors.')
                        break
                else:
                    prev_err=False
                    with open(py_result_file,'w',encoding='UTF8') as f:
                        f.write('\n**stdout:**\n')
                        f.write(str(p.stdout))
                        f.write('\n**stderr:**\n')
                        f.write(str(p.stderr))
                time.sleep(5)
            print('Error total: ',error_total)
        
                