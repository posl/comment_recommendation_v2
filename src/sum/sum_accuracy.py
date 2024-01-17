import csv
import os
import pandas as pd

class Sum_accuracy:
    def __init__(self, base_path, times, language, all_frag):
        self.base_path = base_path
        self.all_frag = all_frag
        if self.all_frag:
            self.result_path = base_path + '/result/accuracy/all/{0}/{1}/'.format(times, language)
        else:
            self.result_path = base_path + '/result/accuracy/top/{0}/{1}/'.format(times, language)
        self.times = times
        self.language = language
        self.each_result_l = sorted(os.listdir('{0}/result/accuracy/each/{1}/{2}/'.format(self.base_path, self.times, self.language)))
    
    def main(self):
        sum_accuracy_l = self.sum_accuracy()
        self.write(sum_accuracy_l)

    def sum_accuracy(self):
        sum_accuracy_l = [[0, 0], [0, 0], [0, 0]]
        for i, each_result in enumerate(self.each_result_l):
            df = pd.read_csv('{0}/result/accuracy/each/{1}/{2}/{3}'.format(self.base_path, self.times, self.language, each_result))
            if not self.all_frag:
                df = df[df['Suggestion'] == 0]
            pass_num = len(df[df['Accuracy'] == 1])
            total_num = len(df)
            if i < 4:
                sum_accuracy_l[0][0] += pass_num
                sum_accuracy_l[0][1] += total_num
            elif i < 21:
                sum_accuracy_l[1][0] += pass_num
                sum_accuracy_l[1][1] += total_num
            else:
                sum_accuracy_l[2][0] += pass_num
                sum_accuracy_l[2][1] += total_num
            print(each_result) 
        return sum_accuracy_l
    
    def write(self, sum_accuracy_l):
        os.makedirs(self.result_path, exist_ok=True)
        with open('{0}/sum_accuracy.csv'.format(self.result_path), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['difficulty',  'pass_num', 'total_num', 'accuracy'])
            for i, difficulty in enumerate(['easy', 'medium', 'hard']):
                writer.writerow([difficulty, sum_accuracy_l[i][0], sum_accuracy_l[i][1], sum_accuracy_l[i][0] / sum_accuracy_l[i][1]])

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
            sum_accuracy = Sum_accuracy(base_path, time, language, False)
            sum_accuracy.main()