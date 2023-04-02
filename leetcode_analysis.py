import glob, re, os
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib.patches import PathPatch
import numpy as np
from config import Config

years, difficulties, problem_types, use_ex_cons=['2016-20','2022'],['easy','medium','hard'],\
    ['Array', 'String', 'Hash Table', 'Sorting'],['desc_ex_con','desc_ex_nocon','desc_noex_nocon']

def get_boxplot_result(model_name:str, root_dir:str):
    def get_leetcode_output(result_file:str) -> dict:
        with open(result_file,'r',encoding='UTF8') as f:
            result=f.read()
            stdout,stderr=[l.strip() for l in result.split('**stdout:**')[1].split('**stderr:**')]
            return {'stdout':stdout, 'stderr':stderr}

    def parse_leetcode_stdout(stdout:str) -> dict:
        out_arr=stdout.split(r'\n')
        types=["Accepted","Wrong Answer","Time Limit Exceeded","Memory Limit Exceeded","Runtime Error","Output Limit Exceeded"]
        correctness=[e for e in types if e in out_arr[0]][0]
        cases_ratio_s=re.search(".* ([0-9]+)/([0-9]+) cases passed",out_arr[1])
        beats_ratio=None
        if 'Your runtime beats' in out_arr[2]: beats_ratio=re.search(".*Your runtime beats (.+?) of python3 submissions",out_arr[2]).group(1)
        else: assert('Your runtime beats' not in stdout)
        cases_ratio=float(cases_ratio_s.group(1))/float(cases_ratio_s.group(2))
        out_dict={'correctness':correctness,'cases_ratio':cases_ratio,'beats_ratio':beats_ratio}    
        return out_dict

    def parse_leetcode_cases(stdout:str) -> dict:
        out_arr=stdout.split(r'\n')
        cases_ratio_s=re.search(".* ([0-9]+)/([0-9]+) cases passed",out_arr[1])
        return float(cases_ratio_s.group(2))  

    def parse_result_path(result_path:str) -> dict:
        year, difficulty, problem_type, problem_fullname, use_ex_con, test_num=os.path.normpath(result_path).split(os.sep)[-6:]
        problem_id, problem_name=problem_fullname.split('-')[0], '-'.join(problem_fullname.split('-')[1:])
        use_ex=('_ex' in use_ex_con)
        use_con=('_con' in use_ex_con)
        test_num=test_num.split('output_')[1].split('_result')[0]
        return {'year':year, 'difficulty':difficulty, 'problem_type':problem_type, 
                'problem_fullname': problem_fullname, 'problem_id':problem_id, 'problem_name':problem_name, 
                'use_ex':use_ex, 'use_con':use_con, 'use_ex_con':use_ex_con, 'test_num':test_num}

    result_files=glob.glob(f'{root_dir}/results/{model_name}/**/*output*result.txt', recursive=True)
    print(len(result_files))
    assert(len(result_files)==2*3*4*10*3*5)
    years, difficulties, problem_types, use_ex_cons=['2016-20','2022'],['easy','medium','hard'],['Array', 'Hash Table', 'Sorting', 'String'],['desc_ex_con','desc_ex_nocon','desc_noex_nocon']
    results_top5={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for result_file in tqdm(result_files):
        metas=parse_result_path(result_file)
        try:
            stdout_dict=parse_leetcode_stdout(get_leetcode_output(result_file)['stdout'])
        except:
            print('Error: ',result_file)
        y,d,pt,uec=metas['year'],metas['difficulty'],metas['problem_type'],metas['use_ex_con']
        pf=metas['problem_fullname']
        if pf not in results_top5[y][d][pt][uec]:
            results_top5[y][d][pt][uec][pf]=dict()
        results_top5[y][d][pt][uec][pf][metas['test_num']]=stdout_dict

    def check_correctness(top5_results:dict, top_k=5) -> int:
        for i in range(1,top_k+1):
            if top5_results[str(i)]['correctness']=='Accepted': return True
        return False

    def get_test_cases_ratio(top5_results:dict, top_k=5) -> float:
        ratios=[]
        for i in range(1,top_k+1):
            ratios.append(top5_results[str(i)]['cases_ratio'])
        return max(ratios)

    def percentage_to_float(percentage:str) -> float:
        return float(percentage.split('%')[0])/100.0

    def float_to_percentage(f:float) -> str:
        return str(int(round(f*100,0)))+'%'

    def get_best_ranking(top5_results:dict, top_k=5) -> float:
        best_beats=0.0
        for i in range(1,top_k+1):
            if top5_results[str(i)]['correctness']=='Accepted': 
                best_beats=max(best_beats, percentage_to_float(top5_results[str(i)]['beats_ratio']))
        return 1-best_beats

    results_summary={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for pt in problem_types:
                for uec in use_ex_cons:
                    for pf in results_top5[yr][d][pt][uec]:
                        results_summary[yr][d][pt][uec][pf]={'correctness':check_correctness(results_top5[yr][d][pt][uec][pf]), 
                                                            'max_cases_ratio':get_test_cases_ratio(results_top5[yr][d][pt][uec][pf]), 
                                                            'best_ranking':get_best_ranking(results_top5[yr][d][pt][uec][pf])}

    def get_average_results(results_summary_t:dict) -> dict:
        correctness_cnt, cases_ratio_sum, best_ranking_sum=0,0.0,0.0
        for pf in results_summary_t:
            correct=results_summary_t[pf]['correctness']
            correctness_cnt+=correct
            if not correct:
                cases_ratio_sum+=results_summary_t[pf]['max_cases_ratio']
            if correct:
                best_ranking_sum+=results_summary_t[pf]['best_ranking']
        mean_cases_ratio_of_failed_ques=cases_ratio_sum/(len(results_summary_t)-correctness_cnt) if correctness_cnt<len(results_summary_t) else 'N/A'
        mean_ranking_of_passed_ques=best_ranking_sum/correctness_cnt if correctness_cnt>0 else 'N/A'
        return {'correctness': f'{correctness_cnt}/{len(results_summary_t)}', 
                'mean_cases_ratio_of_failed_ques':mean_cases_ratio_of_failed_ques, 
                'mean_ranking_of_passed_ques':mean_ranking_of_passed_ques}

    def get_average_results_total(results_summary_d:dict) -> dict:
        correct_list, cases_ratio_list, best_ranking_list=[],[],[]
        for pt in results_summary_d:
            results_summary_t=results_summary_d[pt]
            for pf in results_summary_t:
                correct=results_summary_t[pf]['correctness']
                correct_list.append(correct)
                if not correct:
                    cases_ratio_list.append(results_summary_t[pf]['max_cases_ratio'])
                if correct:
                    best_ranking_list.append(results_summary_t[pf]['best_ranking'])
        mean_cases_ratio_of_failed_ques=sum(cases_ratio_list)/len(cases_ratio_list) if len(cases_ratio_list)>0 else 'N/A'
        mean_ranking_of_passed_ques=sum(best_ranking_list)/len(best_ranking_list) if len(best_ranking_list)>0 else 'N/A'
        return {'correctness': f'{sum(correct_list)}/{len(correct_list)}',
                'mean_cases_ratio_of_failed_ques':mean_cases_ratio_of_failed_ques,
                'mean_ranking_of_passed_ques':mean_ranking_of_passed_ques}
        

    results_summary_avg={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for pt in problem_types:
                for uec in use_ex_cons:
                    results_summary_avg[yr][d][pt][uec]=get_average_results(results_summary[yr][d][pt][uec])
    result_summary_avg_total={yr:{d:{uec:dict() for uec in use_ex_cons} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for uec in use_ex_cons:
                result_summary_avg_total[yr][d][uec]=get_average_results_total({pt:results_summary[yr][d][pt][uec] for pt in problem_types})

    import matplotlib.pyplot as plt
    import numpy as np

    def get_description(path:str, template_path:str, with_examples:bool, with_constraints:bool,
                    remarks='\nPlease implement it in Python. Do not provide any explanation.\n'):
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
            desc=desc+remarks
        with open(template_path,'r',encoding='UTF8') as fr:
            template=fr.read().strip()
            desc=desc+'Start your code from the following template:\n```\n'+template+'\n\n```'
        with open(os.path.dirname(template_path)+"prompt_"+("ex_" if with_examples else "noex_")+("con" if with_constraints else "nocon")+".txt",'w',encoding='UTF8') as fw:
            fw.write(desc)
        return desc

    def get_description_length(yr:str, d:str, pt:str, pf:str, uec:str):
        md_path=get_md_path(yr, d, pt, pf)
        template_path=md_path.replace('README.md','template.py')
        with_examples=uec in ['desc_ex_nocon','desc_ex_con']
        with_constraints=uec in ['desc_noex_con','desc_ex_con']
        return len(get_description(md_path, template_path, with_examples, with_constraints).split())

    def get_md_path(yr:str, d:str, pt:str, pf:str):
        return os.path.join(f"{root_dir}/results/{model_name}", yr, d, pt, pf, 'README.md')

    difficulty_correctness_dict={d:{'correct':[],'incorrect':[]} for d in difficulties}
    for d in difficulties:
        for yr in years:
            for pt in problem_types:
                for uec in use_ex_cons:
                    if uec!='desc_ex_con' or yr!='2022': continue
                    for pf in results_top5[yr][d][pt][uec]:
                        result=results_summary[yr][d][pt][uec][pf]
                        desc_len=get_description_length(yr, d, pt, pf, uec)
                        difficulty_correctness_dict[d]['correct' if result['correctness'] else 'incorrect'].append(desc_len)
    # result=[['easy', 'correct', 150], ['easy', 'incorrect', 200], ...] (difficulty, correctness, description length)
    result=[[k.capitalize(),corr.capitalize(),desc_len] for k,v in difficulty_correctness_dict.items() for corr in ['correct','incorrect'] for desc_len in v[corr]]
    return result

def boxplot_distribution(distribution, y_title, figureName):
    dfl = pd.DataFrame(distribution)
    dfl.columns = ['Level', 'Group', y_title]
    # put H on left side in plot
    if dfl.iloc[0]['Group'] != 'Correct':
        b, c = dfl.iloc[0].copy(), dfl[dfl['Group']=='Correct'].iloc[0].copy()
        dfl.iloc[0], dfl[dfl['Group']=='Correct'].iloc[0] = c, b
    colors = {'Correct': 'white', 'Incorrect': 'grey'}
    fig = plt.figure(figsize=(15, 10))
    plt.xticks(fontsize=31, )
    plt.yticks(fontsize=31, )    
    bp = sns.boxplot(x='Level', y=y_title, data=dfl, showfliers=False, palette=colors, hue='Group', width=0.7, notch=False)
    bp.set_xticklabels(bp.get_xticklabels())
    plt.xlabel('Level', size=42)
    plt.ylabel('Length of prompts', size=42)
    plt.legend(fontsize=28, loc=1)
    adjust_box_widths(fig, 0.8)
    plt.subplots_adjust(bottom=0.2, left=0.1)
    plt.savefig('./' + figureName)
    print('The figure is saved to ./' + figureName)
    plt.show()

    # MWW test
    print()
    length_correct_list = dfl[dfl.iloc[:]['Group'] == 'Correct'][y_title].tolist()
    length_incorrect_list = dfl[dfl.iloc[:]['Group'] == 'Incorrect'][y_title].tolist()
    try:
        hypo = stats.mannwhitneyu(length_correct_list, length_incorrect_list, alternative='two-sided')
        p_value = hypo[1]
    except Exception as e:
        if 'identical' in str(e):
            p_value = 1
    print('p-value: {}'.format(p_value))
    if p_value <= 0.05:
        print('Reject Null Hypothesis: Significantly different!')
    else:
        print('Support Null Hypothesis!')

def adjust_box_widths(g, fac):
    """
    Adjust the widths of a seaborn-generated boxplot.
    """
    # iterating through Axes instances
    for ax in g.axes:
        # iterating through axes artists:
        for c in ax.get_children():

            # searching for PathPatches
            if isinstance(c, PathPatch):
                # getting current width of box:
                p = c.get_path()
                verts = p.vertices
                verts_sub = verts[:-1]
                xmin = np.min(verts_sub[:, 0])
                xmax = np.max(verts_sub[:, 0])
                xmid = 0.5 * (xmin + xmax)
                xhalf = 0.5 * (xmax - xmin)

                # setting new width of box
                xmin_new = xmid - fac * xhalf
                xmax_new = xmid + fac * xhalf
                verts_sub[verts_sub[:, 0] == xmin, 0] = xmin_new
                verts_sub[verts_sub[:, 0] == xmax, 0] = xmax_new

                # setting new width of median line
                for l in ax.lines:
                    if np.all(l.get_xdata() == [xmin, xmax]):
                        l.set_xdata([xmin_new, xmax_new])

def length_analysis():
    config=Config()
    root_dir=os.path.normpath(config.generation_path)                        
    ChatGPT_result=[['ChatGPT '+e[0],e[1],e[2]] for e in get_boxplot_result('ChatGPT', root_dir) if e[0] in ['Easy','Medium']]
    Codex_result=[['Codex '+e[0],e[1],e[2]] for e in get_boxplot_result('Codex', root_dir) if e[0] in ['Easy']]
    result=ChatGPT_result+Codex_result
    boxplot_distribution(result, 'Description length of problems', 'mix_desc_len.jpg')


def draw_table(model_name:str, root_dir, ex_con:str, top_k=5) -> str:
    def get_leetcode_output(result_file:str) -> dict:
        with open(result_file,'r',encoding='UTF8') as f:
            result=f.read()
            stdout,stderr=[l.strip() for l in result.split('**stdout:**')[1].split('**stderr:**')]
            return {'stdout':stdout, 'stderr':stderr}

    def parse_leetcode_stdout(stdout:str) -> dict:
        out_arr=stdout.split(r'\n')
        types=["Accepted","Wrong Answer","Time Limit Exceeded","Memory Limit Exceeded","Runtime Error","Output Limit Exceeded"]
        correctness=[e for e in types if e in out_arr[0]][0]
        cases_ratio_s=re.search(".* ([0-9]+)/([0-9]+) cases passed",out_arr[1])
        beats_ratio=None
        if 'Your runtime beats' in out_arr[2]: beats_ratio=re.search(".*Your runtime beats (.+?) of python3 submissions",out_arr[2]).group(1)
        else: assert('Your runtime beats' not in stdout)
        cases_ratio=float(cases_ratio_s.group(1))/float(cases_ratio_s.group(2))
        out_dict={'correctness':correctness,'cases_ratio':cases_ratio,'beats_ratio':beats_ratio}    
        return out_dict

    def parse_result_path(result_path:str) -> dict:
        year, difficulty, problem_type, problem_fullname, use_ex_con, test_num=os.path.normpath(result_path).split(os.sep)[-6:]
        problem_id, problem_name=problem_fullname.split('-')[0], '-'.join(problem_fullname.split('-')[1:])
        use_ex=('_ex' in use_ex_con)
        use_con=('_con' in use_ex_con)
        test_num=test_num.split('output_')[1].split('_result')[0]
        return {'year':year, 'difficulty':difficulty, 'problem_type':problem_type, 
                'problem_fullname': problem_fullname, 'problem_id':problem_id, 'problem_name':problem_name, 
                'use_ex':use_ex, 'use_con':use_con, 'use_ex_con':use_ex_con, 'test_num':test_num}

    result_files=glob.glob(f'{root_dir}/results/{model_name}/**/*output*result.txt', recursive=True)
    assert(len(result_files)==2*3*4*10*3*top_k)
    years, difficulties, problem_types, use_ex_cons=['2016-20','2022'],['easy','medium','hard'],['Array', 'String', 'Hash Table', 'Sorting'],['desc_ex_con','desc_ex_nocon','desc_noex_nocon']
    results_top5={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for result_file in result_files:
        metas=parse_result_path(result_file)
        try:
            stdout_dict=parse_leetcode_stdout(get_leetcode_output(result_file)['stdout'])
        except Exception as e:
            print(e)
            print('Error: ',result_file)
        y,d,pt,uec=metas['year'],metas['difficulty'],metas['problem_type'],metas['use_ex_con']
        pf=metas['problem_fullname']
        if pf not in results_top5[y][d][pt][uec]:
            results_top5[y][d][pt][uec][pf]=dict()
        results_top5[y][d][pt][uec][pf][metas['test_num']]=stdout_dict

    def check_correctness(top5_results:dict) -> int:
        for i in range(1,top_k+1):
            if top5_results[str(i)]['correctness']=='Accepted': return True
        return False
    
    def get_correct_prob(top5_results:dict) -> int:
        corr_cnt=0
        for i in range(1,top_k+1):
            if top5_results[str(i)]['correctness']=='Accepted': corr_cnt+=1
        corr_prob=corr_cnt/top_k
        return corr_prob

    def get_test_cases_ratio(top5_results:dict) -> float:
        ratios=[]
        for i in range(1,top_k+1):
            ratios.append(top5_results[str(i)]['cases_ratio'])
        return max(ratios)

    def percentage_to_float(percentage:str) -> float:
        return float(percentage.split('%')[0])/100.0

    def float_to_percentage(f:float) -> str:
        return str(int(round(f*100,0)))+'%'

    def get_best_ranking(top5_results:dict) -> float:
        best_beats=0.0
        for i in range(1,top_k+1):
            if top5_results[str(i)]['correctness']=='Accepted': 
                best_beats=max(best_beats, percentage_to_float(top5_results[str(i)]['beats_ratio']))
        return 1-best_beats

    results_summary={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for pt in problem_types:
                for uec in use_ex_cons:
                    for pf in results_top5[yr][d][pt][uec]:
                        results_summary[yr][d][pt][uec][pf]={'correctness':check_correctness(results_top5[yr][d][pt][uec][pf]), 
                                                            'max_cases_ratio':get_test_cases_ratio(results_top5[yr][d][pt][uec][pf]), 
                                                            'best_ranking':get_best_ranking(results_top5[yr][d][pt][uec][pf]),
                                                            'correct_prob':get_correct_prob(results_top5[yr][d][pt][uec][pf])}

    def get_average_results(results_summary_t:dict) -> dict:
        correctness_cnt, cases_ratio_sum, best_ranking_sum, corr_prob_sum=0,0.0,0.0,0.0
        for pf in results_summary_t:
            correct=results_summary_t[pf]['correctness']
            correctness_cnt+=correct
            corr_prob=results_summary_t[pf]['correct_prob']
            corr_prob_sum+=corr_prob
            if not correct:
                cases_ratio_sum+=results_summary_t[pf]['max_cases_ratio']
            if correct:
                best_ranking_sum+=results_summary_t[pf]['best_ranking']
        mean_cases_ratio_of_failed_ques=cases_ratio_sum/(len(results_summary_t)-correctness_cnt) if correctness_cnt<len(results_summary_t) else 'N/A'
        mean_ranking_of_passed_ques=best_ranking_sum/correctness_cnt if correctness_cnt>0 else 'N/A'
        return {'correctness': f'{correctness_cnt}/{len(results_summary_t)}', 
                'mean_cases_ratio_of_failed_ques':mean_cases_ratio_of_failed_ques, 
                'mean_ranking_of_passed_ques':mean_ranking_of_passed_ques,
                'mean_correct_prob':corr_prob_sum/len(results_summary_t)}

    def get_average_results_total(results_summary_d:dict) -> dict:
        correct_list, cases_ratio_list, best_ranking_list, corr_prob_list=[],[],[],[]
        for pt in results_summary_d:
            results_summary_t=results_summary_d[pt]
            for pf in results_summary_t:
                correct=results_summary_t[pf]['correctness']
                correct_list.append(correct)
                corr_prob_list.append(results_summary_t[pf]['correct_prob'])
                if not correct:
                    cases_ratio_list.append(results_summary_t[pf]['max_cases_ratio'])
                if correct:
                    best_ranking_list.append(results_summary_t[pf]['best_ranking'])
        mean_cases_ratio_of_failed_ques=sum(cases_ratio_list)/len(cases_ratio_list) if len(cases_ratio_list)>0 else 'N/A'
        mean_ranking_of_passed_ques=sum(best_ranking_list)/len(best_ranking_list) if len(best_ranking_list)>0 else 'N/A'
        return {'correctness': f'{sum(correct_list)}/{len(correct_list)}',
                'mean_cases_ratio_of_failed_ques':mean_cases_ratio_of_failed_ques,
                'mean_ranking_of_passed_ques':mean_ranking_of_passed_ques,
                'mean_correct_prob':sum(corr_prob_list)/len(corr_prob_list)}
        

    results_summary_avg={yr:{d:{pt:{uec:dict() for uec in use_ex_cons} for pt in problem_types} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for pt in problem_types:
                for uec in use_ex_cons:
                    results_summary_avg[yr][d][pt][uec]=get_average_results(results_summary[yr][d][pt][uec])
    result_summary_avg_total={yr:{d:{uec:dict() for uec in use_ex_cons} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for uec in use_ex_cons:
                result_summary_avg_total[yr][d][uec]=get_average_results_total({pt:results_summary[yr][d][pt][uec] for pt in problem_types})

    def compact_result(year:str, results_summary_avg:dict, result_summary_avg_total:dict):
        dic=results_summary_avg[year]
        total_dic=result_summary_avg_total[year]
        return_dict={d:{pt:dict() for pt in ['total']+problem_types} for d in difficulties}
        for d in difficulties:
            for pt in problem_types:
                return_dict[d][pt]=dic[d][pt][ex_con]
            return_dict[d]['total']=total_dic[d][ex_con]
        return return_dict
    compact_dict={yr: compact_result(yr, results_summary_avg, result_summary_avg_total) for yr in years}
    return compact_dict

def combine_dict_to_lists(dicts:list):
    combined_dict={yr:{d:{pt:{metric:[] for metric in ['correctness', 'mean_cases_ratio_of_failed_ques', 'mean_ranking_of_passed_ques', 'mean_correct_prob']} for pt in ['total']+problem_types} for d in difficulties} for yr in years}
    for yr in years:
        for d in difficulties:
            for pt in ['total']+problem_types:
                for metric in ['correctness', 'mean_cases_ratio_of_failed_ques', 'mean_ranking_of_passed_ques', 'mean_correct_prob']:
                    for dic in dicts:
                        combined_dict[yr][d][pt][metric].append(dic[yr][d][pt][metric])
    return combined_dict

def float_to_percentage(f) -> str:
    if f=='N/A': return ' - '
    else: return str(int(round(f*100,0)))+'\\%'
    
def get_latex_table(combined_dict:dict, yr:str):
    latex_code=""
    latex_code+=r"\begin{table}[t]"+"\n"
    latex_code+="\t"+r"\centering"+"\n"
    latex_code+="\t"+r"\caption{Performance of ChatGPT, Codex, and CodeGen on code generation for the problems in LeetCode "+(yr if yr=='2022' else '2016-2020')+r".}"+"\n"
    latex_code+="\t"+r"\label{tab:code_generation_leetcode_"+yr+r"}"+"\n"
    latex_code+="\t"+r"\resizebox{1\linewidth}{!}"+"\n"
    latex_code+="\t"+r"{"+"\n"
    latex_code+="\t\t"+r"\begin{tabular}{l|l|rrr|rrr}"+"\n"
    latex_code+="\t\t\t"+r"\toprule"+"\n"
    latex_code+="\t\t\t"+r"\multirow{2}{*}{\bf Level} & \multirow{2}{*}{\bf Type} & \multicolumn{3}{c|}{\bf Correctness (Prob.)} & \multicolumn{3}{c}{\bf Avg. Rank }\\\cline{3-8}"+"\n"
    latex_code+="\t\t\t"+r"& & {\bf C.GPT} & {\bf C.dex} & {\bf C.Gen} & {\bf C.GPT} & {\bf C.dex} & {\bf C.Gen} \\"+"\n"
    
    for d in difficulties:
        latex_code+="\t\t\t"+r"\hline"+"\n"
        latex_code+="\t\t\t\t"+r"\multirow{4}{*}{"+d.capitalize()+r"}"+"\n"
        for pt in problem_types:
            correctness_str=' & '.join([e.split('/')[0]+f" ({combined_dict[yr][d][pt]['mean_correct_prob'][i]:.2f})" \
                for i,e in enumerate(combined_dict[yr][d][pt]['correctness'])])
            ranking_str=' & '.join([float_to_percentage(e) for e in combined_dict[yr][d][pt]['mean_ranking_of_passed_ques']])
            latex_code+="\t\t\t"+r"& "+pt+" & "+correctness_str+" & "+ranking_str+r" \\"+"\n"
        latex_code+="\t\t\t"+r"\hline"+"\n"
        correctness_str_total=' & '.join([e.split('/')[0]+f" ({combined_dict[yr][d]['total']['mean_correct_prob'][i]:.2f})" \
            for i,e in enumerate(combined_dict[yr][d]['total']['correctness'])])
        ranking_str_total=' & '.join([float_to_percentage(e) for e in combined_dict[yr][d]['total']['mean_ranking_of_passed_ques']])
        latex_code+="\t\t\t"+r"Total &  & "+correctness_str_total+"  & "+ranking_str_total+r" \\"+"\n"
    latex_code+="\t\t\t"+r"\bottomrule"+"\n"
    latex_code+="\t\t"+r"\end{tabular}"+"\n"
    latex_code+="\t"+r"}"+"\n"
    latex_code+=r"\end{table}"+"\n"
    return latex_code

def get_latex_tables():
    config=Config()
    root_dir=os.path.normpath(config.generation_path)
    chatgpt_dict=draw_table("ChatGPT", root_dir, ex_con='desc_ex_con')
    codex_dict=draw_table("Codex", root_dir, ex_con='desc_ex_con')
    codegen_dict=draw_table("CodeGen", root_dir, ex_con='desc_ex_con')
    combined_dict=combine_dict_to_lists([chatgpt_dict, codex_dict, codegen_dict])
    table1=get_latex_table(combined_dict, '2016-20')
    table2=get_latex_table(combined_dict, '2022')
    print(table1)
    print('\n\n')
    print(table2)
    return table1, table2