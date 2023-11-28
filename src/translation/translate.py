import requests
import os
from dotenv import load_dotenv
load_dotenv('../../.env')

API_KEY = os.getenv('DeepL_API_KEY')

class Translate:
    def __init__(self, base_path, language):
        self.base_path = base_path
        self.language = language

    def main(self):
        input_path = '{0}/data/en/'.format(self.base_path)
        output_path = '{0}/data/{1}/'.format(self.base_path, self.language.lower())
        os.makedirs(output_path, exist_ok=True)

        files_l = os.listdir(input_path)
        files_l = sorted(files_l)
        if '.DS_Store' in files_l:
            files_l.remove('.DS_Store')

        for file in files_l:
            print(file)
            self.translate(input_path + file, output_path + file)

    def translate(self, Input, Output):
        with open(Input, 'r') as f:
            self.source_file_l = f.read()
        url = 'https://api-free.deepl.com/v2/translate'
        params = {
            'auth_key': API_KEY,
            'text': self.source_file_l,
            'source_lang': 'EN',
            'target_lang': self.language
        }

        request = requests.post(url, data=params)
        result = request.json()

        with open(Output, 'w') as f:
            f.write(result['translations'][0]['text'])

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for language in ['JA', 'ZH']:
        translate = Translate(base_path, language)
        translate.main()
