import subprocess
import os
import csv
import shutil
import re

class PreTestScript:
    def __init__(self, Base_path, Times, Language):
        self.times = Times
        self.base_path = Base_path
        self.language = Language
        self.base_script_path = '{0}/script/mod_gen/{1}/{2}/'.format(Base_path, Times, Language)
        self.all_result_path = '{0}/result/ALL/{1}/{2}/'.format(Base_path, Times, Language)
        self.accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(Base_path, Times, Language)
    
    def search_output(self):
        self.pre_result_path = '{0}/result/pre/{1}/{2}'.format(self.base_path, self.times, self.language)
        problem_l = sorted(os.listdir(self.base_script_path))
        if '.DS_Store' in problem_l:
            problem_l.remove('.DS_Store')
        problem_l.sort()
        target = ['09']
        problem_l = target
        for each_problem in problem_l:
            self.problem_number = each_problem
            suggestion_l = sorted(os.listdir('{0}/{1}'.format(self.base_script_path, each_problem)))
            if os.path.exists(self.pre_result_path + '/' + self.problem_number):
                shutil.rmtree(self.pre_result_path + '/' + self.problem_number)
            os.makedirs('{0}/{1}'.format(self.pre_result_path, self.problem_number), exist_ok=True)
            #suggestion_l = [suggestion_l[2]]
            suggestion_l = [suggestion_l[0], suggestion_l[2]]
            for each_suggestion in suggestion_l:
                self.script_path = '{0}/{1}/{2}'.format(self.base_script_path, each_problem, each_suggestion)
                self.suggestion = each_suggestion
                self.input_path = '{0}/test_case/{1}/in/'.format(self.base_path, each_problem)
                self.input_path_l = sorted(os.listdir(self.input_path))
                self.output_path = ('{0}/test_case/{1}/out/'.format(self.base_path, each_problem))
                self.output_path_l = sorted(os.listdir(self.output_path))
                all_test_result_l = self.pre_pyexe()
                self.write_pre_result(all_test_result_l)
                #break
            break
    
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
            '''
            with open(each_test_output_path, encoding='utf-8') as f:
                answer = f.read()
                print(answer)

            if output == answer:
                correct = 1
                print('Correct')
            else:
                correct = 0
                print('Wrong')
            '''
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
    
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    time_l = []
    language_l = []
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
    
    for time in time_l:
        for language in language_l:
            pts = PreTestScript(base_path, time, language)
            pts.search_output()