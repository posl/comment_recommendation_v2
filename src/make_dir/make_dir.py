import os
import shutil

class MakeDir:
    def __init__(self, Base_path, Pre_flag):
        self.base_path = Base_path
        self.pre_flag = Pre_flag

    def test_case_dir(self):
        target_dir = os.listdir('{0}/data/en/'.format(self.base_path))
        target_dir = sorted(list(map(lambda x : x.split('.')[0].split('problems')[1], target_dir)))
        if self.pre_flag == True:
            for dir_name in target_dir:
                path = '{0}/pre_test_case/{1}'.format(self.base_path, dir_name)
                if os.path.exists(path):
                    shutil.rmtree(path)
                os.makedirs('{0}/in'.format(path), exist_ok=True)
                os.makedirs('{0}/out'.format(path), exist_ok=True)
            print('Done')
        return 
    
    def create_sample_txt(self):
        if self.pre_flag == True:
            target_dir = sorted(os.listdir('{0}/pre_test_case/'.format(self.base_path)))
            for each_dir_path in target_dir:
                for number in ['01', '02']:
                    f = open('{0}/test_case/{1}/in/sample_{2}.txt'.format(self.base_path, each_dir_path, number), 'w')
                    f = open('{0}/test_case/{1}/out/sample_{2}.txt'.format(self.base_path, each_dir_path, number), 'w')
        return

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    md = MakeDir(base_path, True)
    md.test_case_dir()
    md.create_sample_txt()