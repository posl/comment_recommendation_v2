import os

class MakeDir:
    def __init__(self, base_path):
        self.base_path = base_path

    def test_case_dir(self):
        target_dir = os.listdir('{0}/data/en/'.format(self.base_path))
        target_dir = sorted(list(map(lambda x : x.split('.')[0].split('problems')[1], target_dir)))
        for dir_name in target_dir:
            path = '{0}/test_case/{1}'.format(self.base_path, dir_name)
            os.makedirs('{0}/in'.format(path), exist_ok=True)
            os.makedirs('{0}/out'.format(path), exist_ok=True)
        print('Done')
        return 

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    md = MakeDir(base_path)
    md.test_case_dir()