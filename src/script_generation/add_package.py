import os

class AddPackage:
    def __init__(self, base_path):
        self.base_path = base_path
    
    def main(self):
        self.add_package('1', 'en', '33', 'collections', 'Counter')
        self.add_package('1', 'en', '24', 'functools', 'cache')
        self.add_package('1', 'en', '15', 'collections', 'deque')
        self.add_package('2', 'en', '15', 'collections', 'deque')
        self.add_package('2', 'en', '22', 'bisect', 'bisect_left')
        self.add_package('3', 'en', '15', 'collections', 'deque')
        self.add_package('4', 'en', '15', 'collections', 'deque')
        self.add_package('4', 'en', '33', 'collections', 'defaultdict')
        self.add_package('5', 'en', '15', 'collections', 'deque')
        self.add_package('5', 'en', '22', 'bisect', 'bisect_left')
        self.add_package('1', 'ja', '15', 'collections', 'deque')
        self.add_package('2', 'ja', '15', 'collections', 'deque')
        self.add_package('3', 'ja', '15', 'collections', 'deque')
        self.add_package('3', 'ja', '23', False, 'math')
        self.add_package('3', 'ja', '33', 'collections', 'defaultdict')
        self.add_package('4', 'ja', '15', 'collections', 'deque')
        self.add_package('4', 'ja', '18', False, 'math')
        self.add_package('4', 'ja', '22', False, 'bisect')
        self.add_package('4', 'ja', '33', 'collections', 'defaultdict')
        self.add_package('5', 'ja', '15', 'collections', 'deque')

    def add_package(self, time, language, problem, from_package, import_package):
        time = str(time) + '_time'
        problem = str(problem).zfill(2)
        with open('{0}/script/mod_gen/{1}/{2}/{3}/0.py'.format(self.base_path, time, language, problem), 'r') as f:
            source_file_l = f.readlines()
            if not 'import' in source_file_l[0]:
                if not from_package:
                    source_file_l.insert(0, 'import {0}\n'.format(import_package))
                else:
                    source_file_l.insert(0, 'from {0} import {1}\n'.format(from_package, import_package))
                with open('{0}/script/mod_gen/{1}/{2}/{3}/0.py'.format(self.base_path, time, language, problem), 'w') as f:
                    for line in source_file_l:
                        f.write(line)
                    
if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    add_package = AddPackage(base_path)
    add_package.main()