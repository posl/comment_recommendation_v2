import subprocess
import os
import csv
import shutil
import re
from modify_txt import ModifyTxt

class PreTestScript:
    def __init__(self, Base_path, Times, Language):
        self.times = Times
        self.base_path = Base_path
        self.language = Language
        self.base_script_path = '{0}/script/mod_gen/{1}/{2}/'.format(Base_path, Times, Language)
        self.all_result_path = '{0}/result/ALL/{1}/{2}/'.format(Base_path, Times, Language)
        self.accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(Base_path, Times, Language)
        self.solution_path = '{0}/leetcode_solution'.format(self.base_path)

    # create solution file without text (run only once)   
    def create_solution_file(self, create_flag):
        if create_flag == True:
            problem_l = sorted(os.listdir(self.base_script_path))
            if '.DS_Store' in problem_l:
                problem_l.remove('.DS_Store')
            problem_l.sort()
            for each_problem in problem_l:
                os.makedirs('{0}/{1}'.format(self.solution_path, each_problem), exist_ok=True)
                f = open('{0}/{1}/solution.py'.format(self.solution_path, each_problem), 'w')
        
    
    def search_output(self):
        self.pre_result_path = '{0}/result/pre/{1}/{2}'.format(self.base_path, self.times, self.language)
        target = int(input('input problem number:'))
        problem_l = [str(target).zfill(2)]

        # modify testcase input 
        ModifyTxt(self.base_path).main(problem_l)
        
        # create testcase output
        for each_problem in problem_l:
            self.problem_number = each_problem
            suggestion_l = sorted(os.listdir('{0}/{1}'.format(self.solution_path, each_problem)))
            if os.path.exists(self.pre_result_path + '/' + self.problem_number):
                shutil.rmtree(self.pre_result_path + '/' + self.problem_number)
            os.makedirs('{0}/{1}'.format(self.pre_result_path, self.problem_number), exist_ok=True)
            for each_suggestion in suggestion_l:
                self.script_path = '{0}/{1}/{2}'.format(self.solution_path, each_problem, each_suggestion)
                self.suggestion = each_suggestion
                self.input_path = '{0}/test_case/{1}/in/'.format(self.base_path, each_problem)
                self.input_path_l = sorted(os.listdir(self.input_path))
                self.output_path = ('{0}/test_case/{1}/out/'.format(self.base_path, each_problem))
                self.output_path_l = sorted(os.listdir(self.output_path))
                # run solution script
                all_test_result_l = self.pre_pyexe()
                # write solution result to csv
                self.write_pre_result(all_test_result_l)
                #break
            #break
            # create testcase output
            self.make_output(each_problem, suggestion_l[0])
    
    def pre_pyexe(self):
        all_test_result = []
        for index, each_test_input in enumerate(self.input_path_l):
            each_test_input_path = '{0}/{1}'.format(self.input_path, self.input_path_l[index])
            each_test_output_path = '{0}/{1}'.format(self.output_path, self.output_path_l[index])
            cmd = 'exec python {0} < {1}'.format(self.script_path, each_test_input_path)
            try:
                process = subprocess.run(cmd, shell = True, capture_output = True, text = True, timeout = 30)
                output = process.stdout
                output = re.sub("b'|'|\\n", '', output)
                message = process.stderr
                #print(output)

            except subprocess.TimeoutExpired:
                message = 'Time Limit Exceeded'
                output = ''
            each_test_result = [self.language, self.problem_number, self.suggestion, self.input_path_l[index].split('.')[0], output, message]
            
            all_test_result.append(each_test_result)
        return all_test_result
    
    def write_pre_result(self, all_test_result_l):
        with open('{0}/{1}/{2}.csv'.format(self.pre_result_path, self.problem_number, self.suggestion.split('.')[0]), 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['language', 'problem_number', 'suggestion', 'test_case', 'output', 'message'])
            for each_test_result in all_test_result_l:
                writer.writerow(each_test_result)
        return
    
    def make_output(self, Problem, Suggestion):
        with open('{0}/{1}/{2}.csv'.format(self.pre_result_path, Problem, Suggestion.split('.')[0]), 'r') as f:
            reader = csv.reader(f)
            content = [row for row in reader]
        for index in range(1, 16):
            with open('{0}/test_case/{1}/out/{2}.txt'.format(self.base_path, Problem, str(index).zfill(2)), 'w') as f:
                if Problem != '32':
                    f.write(content[index][4])
                else:
                    answer = content[index][4]
                    answer = re.sub('\[|\]|,', '', answer)
                    answer = answer.split()
                    answer = str(answer)
                    f.write(answer)
    
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    time_l = ['1_time']
    language_l = ['en']
    '''
    while True:
        time = input('Enter time: 1, 2, 3, 4, 5, or press enter to exit:')
        if time == '':
            break
        time_l.append(time + '_time')
    while True:
        language = input('Enter language: en, ja, zh, or press enter to exit:')
        if language == '':
            break
        language_l.append(language)
    '''
    
    for time in time_l:
        for language in language_l:
            pts = PreTestScript(base_path, time, language)
            pts.search_output()