import os

class FileRename:
    def __init__(self, base_path):
        self.base_path = base_path

    def main(self):
        input_path = '{0}/data/'.format(self.base_path)
        for language in ['en', 'ja', 'zh']:
            input_path = '{0}/data/{1}/'.format(self.base_path, language)
            files_l = os.listdir(input_path)
            files_l = sorted(files_l)
            if '.DS_Store' in files_l:
                files_l.remove('.DS_Store')

            for file in files_l:
                self.rename(input_path, file)

    def rename(self, Input, File):
        if len(File.split('problems')[1].split('.')[0]) == 1:
            number = '0' + File.split('problems')[1].split('.')[0]
            os.rename(Input + File, Input + File.replace(File.split('problems')[1].split('.')[0], number))

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(base_path)
    file_rename = FileRename(base_path)
    file_rename.main()