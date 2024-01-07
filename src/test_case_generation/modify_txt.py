import re
import os

class ModifyTxt:
    def __init__(self, Base_path):
        self.base_path = '{0}/test_case'.format(Base_path)

    def main(self, problem_l):
        for each_problem in problem_l:
            self.modify_txt(each_problem)
            print(each_problem)

    def modify_txt(self, each_problem):
        self.problem_number = each_problem
        self.input_path = '{0}/{1}/in'.format(self.base_path, each_problem)
        self.input_path_l = sorted(os.listdir(self.input_path))
        self.output_path = '{0}/{1}/out'.format(self.base_path, each_problem)
        for index in range(len(self.input_path_l)):
            self.rewrite_txt(self.input_path, self.input_path_l[index])
            #self.rewrite_txt(self.output_path, self.input_path_l[index])
    
    def rewrite_txt(self, Path, Index):
        with open('{0}/{1}'.format(Path, Index), 'r') as f:
            data = f.read()
            data = re.sub('`|\[|\]|,', '', data)
        with open('{0}/{1}'.format(Path, Index), 'w') as f:
            f.write(data)

if __name__ == '__main__':
    Base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace('\\', '/')
    problem_l = ['11']
    ModifyTxt(Base_path).main(problem_l)
