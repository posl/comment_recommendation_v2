import csv
import os
import pandas as pd

class Sum_difficulty:
    def __init__(self, language):
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.result_path = '{0}/result/accuracy/all/{1}'.format(self.base_path, language)
        self.read_path = '{0}/result/accuracy/top'.format(self.base_path)
        self.language = language

    def main(self):
        main_df = self.sum_accuracy()
        self.write(main_df)

    def sum_accuracy(self):
        easy_df = pd.DataFrame()
        medium_df = pd.DataFrame()
        hard_df = pd.DataFrame()
        for i in range(1, 6):
            each_df = pd.read_csv('{0}/{1}_time/{2}/sum_accuracy.csv'.format(self.read_path, str(i), self.language))
            for difficulty in ['easy', 'medium', 'hard']:
                df = each_df[each_df['difficulty'] == difficulty]
                if difficulty == 'easy':
                    easy_df = pd.concat([easy_df, df])
                elif difficulty == 'medium':
                    medium_df = pd.concat([medium_df, df])
                else:
                    hard_df = pd.concat([hard_df, df])
        
        main_df = pd.concat([easy_df, medium_df, hard_df])
        return main_df
    
    def write(self, df):
        os.makedirs(self.result_path, exist_ok=True)
        df.to_csv('{0}/sum_all_accuracy.csv'.format(self.result_path), index=False)

if __name__ == '__main__':
    language_l = []
    while True:
        language = input('Enter language: en, ja, zh, or press enter to exit:')
        if language == '':
            break
        language_l.append(language)
    for language in language_l:
        sum_difficulty = Sum_difficulty(language)
        sum_difficulty.main()