import glob
import os, sys, time, torch, openai
from chatgpt_wrapper import ChatGPT
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config
from leetcode_util import LeetCodeUtil

class GenerationUtil:
    def __init__(self, model_name):
        self.model_name = model_name
        if model_name == "ChatGPT":
            self.chatbot = ChatGPT()
        elif model_name == "CodeGen":
            self.model, self.tokenizer, self.device = self.load_model("Salesforce/codegen-2B-mono")
        elif model_name == "Codex":
            config=Config()
            openai.api_key = config.openai_api_key
            openai.organization = config.openai_organization
            
    
    def load_model(self, checkpoint):
        device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)
        model.eval()
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        return model, tokenizer, device
    
    def generate(self, prompt, max_length=1024):
        if self.model_name == "ChatGPT": return self.generate_chatgpt(prompt)
        elif self.model_name == "Codex": return self.generate_codex(prompt, max_length)
        elif self.model_name == "CodeGen": return self.generate_codegen(prompt, max_length)
        else: assert False, "Invalid model name"
    
    def generate_all(self, with_examples:bool, with_constraints:bool, \
        remarks='Implement the above task in Python.', max_length=1024, repetition=5):
        def output_exists(out_path:str):
            if os.path.exists(out_path):
                with open(out_path,'r',encoding='UTF8') as fr:
                    content=fr.read()
                    if content.strip()=='':
                        return False
                    return True
        config=Config()
        root_path=os.path.normpath(config.generation_path)
        md_paths=glob.glob(root_path+'/results/'+self.model_name+'/**/README.md', recursive=True)
        for md_path in md_paths:
            problem_path=os.path.dirname(md_path)
            template_path=md_path.replace('README.md','template.py')
            prompt=self.get_description(md_path, template_path, with_examples, with_constraints, remarks)
            response=self.generate(prompt, max_length)
            output_folder='desc_'+('ex' if with_examples else 'noex')+'_'+('con' if with_constraints else 'nocon')
            output_dir=os.path.join(problem_path,output_folder)
            if not os.path.exists(output_dir): os.mkdir(output_dir)
            for i in range(1,repetition+1):
                output_path=output_dir+'/output_'+str(i)+'.txt'
                if output_exists(output_path): continue
                print(f'Asking {self.model_name}...')
                curr_time=time.time()
                response=self.generate(prompt, max_length)
                time_used=time.time()-curr_time
                print(f'{self.model_name} response received.')
                with open(output_path,'w',encoding='UTF8') as f:
                    f.write(response)
                    print('Response written to',output_path)
                print('Time used:',time_used)
                py_file_path=LeetCodeUtil().generate_submit_file(output_path, self.model_name)
                LeetCodeUtil().remove_leetcode_result(py_file_path)
                
    def generate_chatgpt(self, prompt):
        resp='Unusable response produced by ChatGPT, maybe its unavailable.'
        fail_cnt=0
        chatbot=self.chatbot
        while 'Unusable response produced by ChatGPT, maybe its unavailable.' in resp:
            resp=chatbot.ask(prompt)
            chatbot.new_conversation() # To start a new conversation
            if fail_cnt==0: pass
            elif fail_cnt==5:
                print('Failed',fail_cnt,'time(s).')
                print('Exit program.')
                sys.exit()
            else:
                print('Failed',fail_cnt,'time(s).')
                print("Wait for",2**(fail_cnt-1),"seconds.")
                time.sleep(2**(fail_cnt-1))
            fail_cnt+=1
        return resp
    
    def generate_codex(self, prompt, max_length=1024):
        try:
            resp=openai.Completion.create(engine="code-davinci-002", prompt=prompt,max_tokens=max_length)
            resp=prompt+resp.choices[0].text
            return resp
        except Exception as e:
            print(e)
            sys.exit()
    
    def generate_codegen(self, prompt, max_length=1024):
        model, tokenizer, device = self.model, self.tokenizer, self.device
        with torch.no_grad():
            completion = model.generate(**(tokenizer(prompt, return_tensors="pt")).to(device), \
                max_length=max_length, do_sample=True)
            answer = tokenizer.decode(completion[0])
        return answer
    
    def get_description(self, path:str, template_path:str, \
        with_examples:bool, with_constraints:bool, remarks='Implement the above task in Python.'):
        desc=None
        with open(path,'r',encoding='UTF8') as fr:
            prob=fr.read()
            desc=prob.split('## Description')[1].split('**Example')[0]
            if with_examples:
                try:
                    desc=desc+'**Example 1:**'+prob.split('**Example 1:**')[1].split('**Constraints:**')[0]
                except:
                    desc=desc+'**Example:**'+prob.split('**Example:**')[1].split('**Constraints:**')[0]
            if with_constraints:
                desc=desc+'**Constraints:**'+prob.split('**Constraints:**')[1].split('**Tags:**')[0]
        with open(template_path,'r',encoding='UTF8') as fr:
            template=fr.read().strip()
            desc+='\n```\n'+template+'\n```'
        desc+=remarks
        if self.model_name!="ChatGPT":
            desc="'''\n'+desc+'\n'''\n"+template
            desc+='\n'+'\n'.join(
                [l for l in template.split('\n') if l.strip()!='' \
                    and (not l.strip().startswith('#'))][:2])
        return desc