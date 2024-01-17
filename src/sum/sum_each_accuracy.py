import csv
import os
import pandas as pd

class Sum_each_accuracy:
    def __init__(self, base_path, times, language, all_frag):
        self.base_path = base_path
        self.all_frag = all_frag
        if self.all_frag:
            self.result_path = '{0}/result/accuracy/all/{1}/{2}/'.format(base_path, times, language)
        else:
            self.result_path = '{0}/result/accuracy/top/{1}/{2}/'.format(base_path, times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))
        
    def main(self):
        all_result_l = self.sum_accuracy()
        self.write(all_result_l)
    
    def sum_accuracy(self):
        all_result_l = []
        for each_result in self.each_result_l:
            main_df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))
            problem_number = each_result.split('_')[0]
            if not self.all_frag:
                df = main_df[main_df['Suggestion'] == 0]
            pass_num = len(df[df['Accuracy'] == 1])
            total_num = len(df)
            if (pass_num == total_num) and (pass_num != 0):
                each_result_l = [problem_number, pass_num, total_num, 1]
            elif pass_num == 0:
                each_result_l = [problem_number, pass_num, total_num, 0]
            else:
                each_result_l = [problem_number, pass_num, total_num]
            all_result_l.append(each_result_l)
            print(each_result) 
        return all_result_l
    
    def write(self, all_result_l):
        os.makedirs(self.result_path, exist_ok=True)
        with open('{0}/sum_each_accuracy.csv'.format(self.result_path), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['problem_number', 'pass_num', 'total_num', 'accuracy'])
            for each_result_l in all_result_l:
                writer.writerow(each_result_l)

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
            sum_accuracy = Sum_each_accuracy(base_path, time, language, False)
            sum_accuracy_l = sum_accuracy.sum_accuracy()
            sum_accuracy.write(sum_accuracy_l)
    
