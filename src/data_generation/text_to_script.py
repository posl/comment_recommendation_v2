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
                self.create_script(input_path + file, output_path + file.replace('.txt', '.py'), file.split('.')[0].replace('problems', ''))

    def create_output_dir(self, base_path, dir_l):
        for dir_name in dir_l:
            path = '{0}/{1}'.format(base_path, dir_name)
            os.makedirs(path, exist_ok=True)
            base_path = path 
    
    def create_script(self, Input, Output, Problem):
        with open(Input, 'r') as f:
            source_file_l = f.readlines()
            source_file_l = list(map(lambda x: '#' + x, source_file_l))
            #source_file_l.append('\n\ndef ')
            self.add_class(source_file_l, Problem)

        with open(Output, 'w') as f:
            for line in source_file_l:
                f.write(line)
    
    def add_class(self, source_file_l, Problem):
        if Problem != '15':
            source_file_l.append('\nclass Solution:\n')

        if Problem == '01':
            source_file_l.append('    def twoSum(self, nums: list[int], target: int) -> list[int]:\n')
        elif Problem == '02':
            source_file_l.append('    def generate(self, numRows: int) -> list[list[int]]:\n')
        elif Problem == '03':    
            source_file_l.append('    def getRow(self, rowIndex: int) -> list[int]:\n')
        elif Problem == '04':
            source_file_l.append('    def countBits(self, n: int) -> list[int]:\n')
        elif Problem == '05':
            source_file_l.append('    def findSubstringInWraproundString(self, s: str) -> int:\n')
        elif Problem == '06':
            source_file_l.append('    def nthUglyNumber(self, n: int) -> int:\n')
        elif Problem == '07':
            source_file_l.append('    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:\n')
        elif Problem == '08':
            source_file_l.append('    def maxRotateFunction(self, nums: list[int]) -> int:\n')
        elif Problem == '09':
            source_file_l.append('    def canPartition(self, nums: list[int]) -> bool:\n')
        elif Problem == '10':
            source_file_l.append('    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:\n')
        elif Problem == '11':
            source_file_l.append('    def lengthOfLIS(self, nums: list[int]) -> int:\n')
        elif Problem == '12':
            source_file_l.append('    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:\n')
        elif Problem == '13':
            source_file_l.append('    def integerReplacement(self, n: int) -> int:\n')
        elif Problem == '14':
            source_file_l.append('    def integerBreak(self, n: int) -> int:\n')
        elif Problem == '15':
            source_file_l.append('\n\n# Definition for a binary tree node.\n')
            source_file_l.append('# class TreeNode(object):\n')
            source_file_l.append('#     def __init__(self, val=0, left=None, right=None):\n')
            source_file_l.append('#         self.val = val\n')
            source_file_l.append('#         self.left = left\n')
            source_file_l.append('#         self.right = right\n')
            source_file_l.append('class Solution(object):\n')
            source_file_l.append('    def buildTree(self, inorder, postorder):\n')
            source_file_l.append('        """\n')
            source_file_l.append('        :type inorder: list[int]\n')
            source_file_l.append('        :type postorder: list[int]\n')
            source_file_l.append('        :rtype: TreeNode\n')
            source_file_l.append('        """\n')
        elif Problem == '16':
            source_file_l.append('    def combinationSum4(self, nums: list[int], target: int) -> int:\n')
        elif Problem == '17':
            source_file_l.append('    def coinChange(self, coins: list[int], amount: int) -> int:\n')
        elif Problem == '18':
            source_file_l.append('    def countNumbersWithUniqueDigits(self, n: int) -> int:\n')
        elif Problem == '19':
            source_file_l.append('    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:\n')
        elif Problem == '20':
            source_file_l.append('    def maxProfit(self, prices: list[int]) -> int:\n')
        elif Problem == '21':
            source_file_l.append('    def numberOfArithmeticSlices(self, nums: list[int]) -> int:\n')
        elif Problem == '22':
            source_file_l.append('    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:\n')
        elif Problem == '23':
            source_file_l.append('    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:\n')
        elif Problem == '24':
            source_file_l.append('    def numDistinct(self, s: str, t: str) -> int:\n')
        elif Problem == '25':
            source_file_l.append('    def maxCoins(self, nums: list[int]) -> int:\n')
        elif Problem == '26':
            source_file_l.append('    def splitArray(self, nums: list[int], k: int) -> int:\n')
        elif Problem == '27':
            source_file_l.append('    def countDigitOne(self, n: int) -> int:\n')
        elif Problem == '28':
            source_file_l.append('    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:\n')
        elif Problem == '29':
            source_file_l.append('    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:\n')
        elif Problem == '30':
            source_file_l.append('    def canCross(self, stones: list[int]) -> bool:\n')
        elif Problem == '31':
            source_file_l.append('    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:\n')
        elif Problem == '32':
            source_file_l.append('    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:\n')
        elif Problem == '33':
            source_file_l.append('    def numberOfArithmeticSlices(self, nums: list[int]) -> int:\n')

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
    