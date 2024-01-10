import os 
import shutil

class AddFunction:
    def __init__(self, base_path, time_l, language_l):
        self.base_path = base_path
        self.time_l = time_l
        self.language_l = language_l

    def main(self):
        os.makedirs('{0}/script/mod_gen/'.format(self.base_path), exist_ok=True)

        for time in self.time_l:
            for language in self.language_l:
                print('===== {0} {1} ====='.format(time, language))
                input_path = '{0}/script/split_gen/{1}/{2}'.format(self.base_path, time, language)
                output_path = '{0}/script/mod_gen/{1}/{2}'.format(self.base_path, time, language)
                if os.path.exists(output_path):
                    shutil.rmtree(output_path)
                os.makedirs(output_path, exist_ok=True)
                problem_dir_l = os.listdir(input_path)
                if 'errors.txt' in problem_dir_l:
                    problem_dir_l.remove('errors.txt')
                problem_dir_l = sorted(problem_dir_l)
                self.add_function(input_path, output_path, problem_dir_l)

    def add_function(self, Input, Output, Problem_Dir):
        for each_dir in Problem_Dir:
            os.mkdir('{0}/{1}'.format(Output, each_dir))
        
            files_l = os.listdir('{0}/{1}'.format(Input, each_dir))
            files_l = sorted(files_l)

            for file in files_l:
                with open('{0}/{1}/{2}'.format(Input, each_dir, file), 'r') as f:
                    source_file_l = f.readlines()
                    try:
                        if source_file_l[0].split(' ')[0] == 'def':
                            function_name = source_file_l[0].split(' ')[1].split('(')[0]
                            argument = source_file_l[0].split('(')[1].split(')')[0]
                            each_argument_l = argument.replace(' ', '').split(',')
                            if (function_name in source_file_l[-1]) and not('return' in source_file_l[-1]) and not('append' in source_file_l[-1]): #and not('print' in script_l[-1])
                                pass
                            else:
                                source_file_l.append('\nif __name__ == \'__main__\':\n')
                                for each_argument in each_argument_l:
                                    compliment = self.add_input(each_argument, each_dir)
                                    source_file_l.append('    {0} = {1}'.format(each_argument, compliment))
                                source_file_l.append('    a = {0}({1})\n    print(a)'.format(function_name, argument))
                            
                        with open('{0}/{1}/{2}'.format(Output, each_dir, file), 'w') as f:
                            for line in source_file_l:
                                f.write(line)
                    except:
                        pass
            print(each_dir)
    
    def add_input(self, Argument, Each_dir):
        if (Argument == 'nums') or (Argument == 'primes') or (Argument == 'inorder') or (Argument == 'postorder') or (Argument == 'coins') or (Argument == 'prices') or (Argument == 'stones'):
            return 'list(map(int, input().split()))\n'
        elif (Argument == 'words'):
            return 'input().split()\n'
        elif (Argument == 'num') or (Argument == 'target') or (Argument == 'n') or (Argument == 's') or (Argument == 't') or (Argument == 'k') or (Argument == 'amount') or (Argument == 'n1') or (Argument == 'n2'):
            if Each_dir == '05':
                return 'input()\n'
            else:
                return 'int(input())\n'
        elif (Argument == 'numRows') or (Argument == 'rowIndex') or (Argument == 'maxChoosableInteger') or (Argument == 'desiredTotal') or (Argument == 'buckets') or (Argument == 'minutesToDie') or (Argument == 'minutesToTest'):
            return 'int(input())\n'
        elif (Argument == 's1') or (Argument == 's2'):
            return 'input()\n'
        #elif (Argument == 'intervals') or (Argument == 'envelopes'):
        #elif (Argument == 'matrix):
        elif Each_dir == '10':
            return 'list(map(int, input().split()))\n    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]\n'
        elif Each_dir == '22':
            return 'list(map(int, input().split()))\n    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]\n'
        else:
            return '==========please modify============\n'
        

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
    af = AddFunction(base_path, time_l, language_l)
    af.main()