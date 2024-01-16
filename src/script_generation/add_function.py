import os 
import shutil
from add_package import AddPackage

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
            files_l = [files_l[0]]
            for file in files_l:
                with open('{0}/{1}/{2}'.format(Input, each_dir, file), 'r') as f:
                    source_file_l = f.readlines()
                    try:
                        # source_file_l = list(map(lambda x: '    ' + x, source_file_l))
                        #if source_file_l[0].split(' ')[0] == 'def':
                        if 'def ' in source_file_l[0]:
                            function_name = source_file_l[0].split(' ')[1].split('(')[0]
                            source_file_l[0] = '    ' + source_file_l[0]
                            argument = source_file_l[0].split('(')[1].split(')')[0]
                            each_argument_l = argument.replace(' ', '').split(',')
                            each_argument_l = list(map(lambda x: x.split(':')[0], each_argument_l))
                            if 'self' in each_argument_l:
                                each_argument_l.remove('self')
                            new_argument = ''
                            for index, each_argument in enumerate(each_argument_l):
                                if index == len(each_argument_l) - 1:
                                    new_argument += '{0}'.format(each_argument)
                                else:
                                    new_argument += '{0}, '.format(each_argument)
                            if (function_name in source_file_l[-1]) and not('return' in source_file_l[-1]) and not('append' in source_file_l[-1]): #and not('print' in script_l[-1])
                                pass
                            else:
                                # problem != 15 -> add class Solution:\n
                                # problem == 15 -> add class TreeNode and class Solution(object):\n
                                class_l = self.add_class(each_dir)
                                source_file_l = class_l + source_file_l
                                source_file_l.append('\nif __name__ == \'__main__\':\n')
                                # for matrix
                                if (each_dir == '28') or (each_dir == '29'):
                                    source_file_l.append('    N, M = map(int, input().split())\n')
                                for each_argument in each_argument_l:
                                    compliment = self.add_input(each_argument, each_dir)
                                    source_file_l.append('    {0} = {1}'.format(each_argument, compliment))
                                #source_file_l.append('    a = {0}({1})\n    print(a)'.format(function_name, new_argument))
                                source_file_l.append('    a = Solution()\n    print(a.{0}({1}))'.format(function_name, new_argument))
                            
                        with open('{0}/{1}/{2}'.format(Output, each_dir, file), 'w') as f:
                            for line in source_file_l:
                                f.write(line)
                    except:
                        pass
            print(each_dir)
    
    def add_class(self, Each_dir):
        source_file_l = []
        if Each_dir == '15':
            source_file_l.append('class TreeNode(object):\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n')
        source_file_l.append('class Solution:\n')
        return source_file_l
    
    def add_input(self, Argument, Each_dir):
        if (Argument == 'nums') or (Argument == 'primes') or (Argument == 'inorder') or (Argument == 'postorder') or (Argument == 'coins') or (Argument == 'prices') or (Argument == 'stones'):
            return 'list(map(int, input().split()))\n'
        elif (Argument == 'words'):
            return 'input().split()\n'
        elif (Argument == 'num') or (Argument == 'target') or (Argument == 'n') or (Argument == 's') or (Argument == 't') or (Argument == 'k') or (Argument == 'amount') or (Argument == 'n1') or (Argument == 'n2'):
            if (Each_dir == '05') or (Each_dir == '24'):
                return 'input()\n'
            else:
                return 'int(input())\n'
        elif (Argument == 'numRows') or (Argument == 'rowIndex') or (Argument == 'maxChoosableInteger') or (Argument == 'desiredTotal') or (Argument == 'buckets') or (Argument == 'minutesToDie') or (Argument == 'minutesToTest'):
            return 'int(input())\n'
        elif (Argument == 's1') or (Argument == 's2'):
            return 'input()\n'
        #elif (Argument == 'intervals') or (Argument == 'envelopes'):
        #elif (Argument == 'matrix):
        elif Each_dir == '10': # Argument == 'intervals'
            return 'list(map(int, input().split()))\n    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]\n'
        elif Each_dir == '22': # Argument == 'envelopes'
            return 'list(map(int, input().split()))\n    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]\n'
        elif Argument == 'matrix':
            return '[list(map(int, input().split())) for _ in range(N)]\n'
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
    add_package = AddPackage(base_path)
    add_package.main()