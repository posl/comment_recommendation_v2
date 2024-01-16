import subprocess
import os
import csv
import shutil
import re

class TestScript:
    def __init__(self, Base_path, Times, Language):
        self.times = Times
        self.base_path = Base_path
        self.language = Language
        self.base_script_path = '{0}/script/mod_gen/{1}/{2}/'.format(Base_path, Times, Language)
        self.all_result_path = '{0}/result/ALL/{1}/{2}/'.format(Base_path, Times, Language)
        self.accu_result_path = '{0}/result/accuracy/each/{1}/{2}/'.format(Base_path, Times, Language)
    
    def main(self):
        self.delete_result(self.all_result_path)
        self.delete_result(self.accu_result_path)
        problem_l = sorted(os.listdir(self.base_script_path))
        if '.DS_Store' in problem_l:
            problem_l.remove('.DS_Store')
        problem_l.sort()
        for each_problem in problem_l:
            self.problem_number = each_problem
            suggestion_l = sorted(os.listdir('{0}/{1}'.format(self.base_script_path, each_problem)))
            suggestion_l = [suggestion_l[0]]
            for each_suggestion in suggestion_l:
                self.script_path = '{0}/{1}/{2}'.format(self.base_script_path, each_problem, each_suggestion)
                self.suggestion = each_suggestion
                self.input_path = '{0}/test_case/{1}/in/'.format(self.base_path, each_problem)
                self.input_path_l = sorted(os.listdir(self.input_path))
                self.output_path = ('{0}/test_case/{1}/out/'.format(self.base_path, each_problem))
                self.output_path_l = sorted(os.listdir(self.output_path))
                all_test_result_l, accuracy_l = self.pyexe()
                self.write_result(all_test_result_l, accuracy_l)
            print('======= {0} {1} ======='.format(self.language, self.problem_number))
    
    def delete_result(self, Path):
        if os.path.exists(Path):
            shutil.rmtree(Path)
        os.makedirs(Path, exist_ok=True)
        return
    
    def pyexe(self):
        all_test_result = []
        accuracy_l = [self.language, self.problem_number, self.suggestion]
        accuracy = 0
        for index, each_test_input in enumerate(self.input_path_l):
            each_test_input_path = '{0}/{1}'.format(self.input_path, self.input_path_l[index])
            each_test_output_path = '{0}/{1}'.format(self.output_path, self.output_path_l[index])
            cmd = 'exec python {0} < {1}'.format(self.script_path, each_test_input_path)
            try:
                process = subprocess.run(cmd, shell = True, capture_output = True, text = True, timeout = 30)
                output = process.stdout
                output = output.encode('utf-8')
                message = process.stderr

            except subprocess.TimeoutExpired:
                message = 'Time Limit Exceeded'
                output = ''
            
            with open(each_test_output_path, encoding='utf-8') as f:
                answer = f.read()

            if output == answer:
                correct = 1
            else:
                correct = 0
            accuracy += correct

            if index == len(self.input_path_l) - 1:
                per_accuracy = accuracy / len(self.input_path_l)
                each_test_result = [self.language, self.problem_number, self.suggestion, self.input_path_l[index].split('.')[0], correct, output, answer, message, per_accuracy]
                accuracy_l.append(accuracy)
                accuracy_l.append(len(self.input_path_l))
                accuracy_l.append(per_accuracy)
            else:
                each_test_result = [self.language, self.problem_number, self.suggestion, self.input_path_l[index].split('.')[0], correct, output, answer, message]
            
            all_test_result.append(each_test_result)
        return all_test_result, accuracy_l
    
    def write_result(self, All_test_result, Accuracy_l):
        with open('{0}/{1}.csv'.format(self.all_result_path, self.problem_number, 'a')) as f:
            writer = csv.writer(f)
            if self.suggestion == '0':
                writer.writerow(['Language', 'Problem_number', 'Suggestion', 'Test_case', 'Correct', 'Output', 'Answer', 'Message', 'Accuracy'])
            writer.writerows(All_test_result)
        
        with open('{0}/{1}_accuracy.csv'.format(self.accu_result_path, self.problem_number, 'a')) as f:
            writer = csv.writer(f)
            if self.suggestion == '0':
                writer.writerow(['Language', 'Problem_number', 'Suggestion', 'Test_case_num', 'Total_test_case', 'Accuracy'])
            writer.writerow(Accuracy_l)
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
            ts = TestScript(base_path, time, language)
            ts.main()
    