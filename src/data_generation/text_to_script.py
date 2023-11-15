import os
import shutil

class TextToScript:
    def __init__ (self, base_path, language_l):
        self.base_path = base_path
        self.language_l = language_l

    def main(self):
        # Create output folder
        os.makedirs('{0}/script/pre_gen/'.format(self.base_path), exist_ok=True)

        for language in self.language_l:
            input_path = '{0}/data/{1}/'.format(self.base_path, language)
            output_path = '{0}/script/pre_gen/{1}/'.format(self.base_path, language)
            if os.path.exists(output_path):
                shutil.rmtree(output_path)
            os.makedirs(output_path, exist_ok=True)
            files_l = os.listdir(input_path)
            files_l = sorted(files_l)
            if '.DS_Store' in files_l:
                files_l.remove('.DS_Store')
            for file in files_l:
                self.create_script(input_path + file, output_path + file.replace('.txt', '.py'))

    def create_output_dir(self, base_path, dir_l):
        for dir_name in dir_l:
            path = '{0}/{1}'.format(base_path, dir_name)
            os.makedirs(path, exist_ok=True)
            base_path = path 
    
    def create_script(self, Input, Output):
        with open(Input, 'r') as f:
            source_file_l = f.readlines()
            source_file_l = list(map(lambda x: '#' + x, source_file_l))
            source_file_l.append('\n\ndef ')

        with open(Output, 'w') as f:
            for line in source_file_l:
                f.write(line)


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    language_l = []
    while True:
        language = input('Enter language: en, ja, zh, or press enter to exit:')
        if language == '':
            break
        language_l.append(language)
    tts = TextToScript(base_path, language_l)
    tts.main()
    