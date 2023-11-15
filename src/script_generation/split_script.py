import os
import shutil

class SplitScript:
    def __init__(self, base_path, time_l, language_l):
        self.base_path = base_path
        self.time_l = time_l
        self.language_l = language_l

    def main(self):
        os.makedirs('{0}/script/split_gen/'.format(self.base_path), exist_ok=True)

        for time in self.time_l:
            for language in self.language_l:
                print('===== {0} {1} ====='.format(time, language))
                input_path = '{0}/script/post_gen/{1}/{2}'.format(self.base_path, time, language)
                output_path = '{0}/script/split_gen/{1}/{2}'.format(self.base_path, time, language)
                if os.path.exists(output_path):
                    shutil.rmtree(output_path)
                os.makedirs(output_path, exist_ok=True)
                files_l = os.listdir(input_path)
                files_l = sorted(files_l)
                for file in files_l:
                    num_dif = (file.split('problems')[1].split('.py')[0]).upper()
                    self.split_script(input_path, output_path, file, num_dif)

    def split_script(self, Input, Output, File, Num_Dif):
        os.mkdir('{0}/{1}'.format(Output, Num_Dif))
        with open('{0}/{1}'.format(Input, File), 'r') as f:
            try:
                for i in range(4):
                        next(f)
                source_file_l = f.readlines()
                source_file_l = list(map(lambda x: x.lstrip('\n'), source_file_l))
                source_file_l = [i for i in source_file_l if not 'Suggestion' in i]
                source_file_l = list(filter(None, source_file_l))
                detect_sign_index_l = self.detect_sign(source_file_l)

                all_script_l = self.each_script(source_file_l, detect_sign_index_l)

                for index, each_script_l in enumerate(all_script_l):
                    with open('{0}/{1}/{2}.py'.format(Output, Num_Dif, str(index)), 'w') as f:
                        for line in each_script_l:
                            f.write(line)
                print(File)
            except:
                index = 0
                if os.path.exists('{0}/errors.txt'.format(Output)):
                    with open('{0}/errors.txt'.format(Output), 'w') as f:
                        f.write(File + '\n')
                    with open('{0}/{1}/{2}.py'.format(Output, Num_Dif, str(index)), 'w') as f:
                        f.write('#')
                else:
                    with open('{0}/errors.txt'.format(Output), 'a') as f:
                        f.write(File + '\n')
                    with open('{0}/{1}/{2}.py'.format(Output, Num_Dif, str(index)), 'w') as f:
                        f.write('#')

    def detect_sign(self, l):
        index_l = []
        for index, content in enumerate(l):
            if content == '=======\n':
                index_l.append(index)
        return index_l
    
    def each_script(self, base_l, l):
        script_l = []
        begin = 0
        for end in l:
            script_l.append(base_l[begin:end])
            begin = end + 1
        script_l.append(base_l[begin:])
        return script_l
    
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
    ss = SplitScript(base_path, time_l, language_l)
    ss.main()