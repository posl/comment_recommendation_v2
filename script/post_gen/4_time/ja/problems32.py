Synthesizing 10/10 solutions

=======
Suggestion 1

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key = len)
        res = []
        wordset = set()
        for word in words:
            if self.dfs(word, wordset):
                res.append(word)
            wordset.add(word)
        return res

=======
Suggestion 2

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # 1. 単語を長さ順にソート
        words.sort(key=len)
        # 2. 単語を順に見ていく
        result = []
        for word in words:
            # 3. 単語を構成する単語を探す
            if self.isConcatenated(word, words):
                result.append(word)
        return result

=======
Suggestion 3

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        wordset = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordset and suffix in wordset:
                    memo[word] = True
                    break
                if prefix in wordset and dfs(suffix):
                    memo[word] = True
                    break
            return memo[word]
        return [word for word in words if dfs(word)]

=======
Suggestion 4

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # メモ化再帰
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and suffix in words:
                    memo[word] = True
                    break
                if prefix in words and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in words and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
        return [word for word in words if dfs(word)]

=======
Suggestion 5

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # 1 <= words.length <= 10^4
        # 1 <= words[i].length <= 30
        # words[i] は英小文字のみで構成される。
        # 単語の文字列はすべて一意である。
        # 1 <= sum(words[i].length) <= 10^5
        # 連結された単語とは、与えられた配列に含まれる少なくとも2つの短い単語(相異なる必要はない)で完全に構成される文字列と定義する。
        # 1. wordsを昇順にソートする
        # 2. 2つの単語を選択する
        # 3. 2つの単語を連結した文字列がwordsに含まれているかを検証する
        # 4. 含まれていれば、出力配列に追加する
        # 5. wordsの最後まで繰り返す
        # 6. 出力配列を返却する
        words.sort(key=lambda x: len(x))
        output = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]):
                    continue
                if words[i] + words[j] in words:
                    output.append(words[i] + words[j])
        return output

=======
Suggestion 6

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        #words.sort(key = lambda x: len(x))
        #print(words)
        #print(words[0])
        #print(words[0][0])
        #print(words[0][1])
        #print(words[0][2])
        #print(words[0][3])
        #print(words[0][4])
        #print(words[0][5])
        #print(words[0][6])
        #print(words[0][7])
        #print(words[0][8])
        #print(words[0][9])
        #print(words[0][10])
        #print(words[0][11])
        #print(words[0][12])
        #print(words[0][13])
        #print(words[0][14])
        #print(words[0][15])
        #print(words[0][16])
        #print(words[0][17])
        #print(words[0][18])
        #print(words[0][19])
        #print(words[0][20])
        #print(words[0][21])
        #print(words[0][22])
        #print(words[0][23])
        #print(words[0][24])
        #print(words[0][25])
        #print(words[0][26])
        #print(words[0][27])
        #print(words[0][28])
        #print(words[0][29])
        #print(words[0][30])
        #print(words[0][31])
        #print(words[0][32])
        #print(words[0][33])
        #print(words[0][34])
        #print(words[0][35])
        #print(words[0][36])
        #print(words[0][37])
        #print(words[0][38])
        #print(words[0][39])
        #print(words[0][40])
        #print(words[0][41])
        #print(words[0][42])
        #print(words[0][43])
        #print(words[0][44])
        #print(words[0][45])
        #print(words[0][46])
        #print(words[0][47])
        #print(words[0][48])
        #print(words[0][49])
        #print(words[0][50])
        #print(words[0][51])
        #print(words[0][

=======
Suggestion 7

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def dfs(word, word_set, memo):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and suffix in word_set:
                    memo[word] = True
                    break
                if prefix in word_set and dfs(suffix, word_set, memo):
                    memo[word] = True
                    break
            return memo[word]

        word_set = set(words)
        memo = {}
        return [word for word in words if dfs(word, word_set, memo)]

=======
Suggestion 8

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x: len(x))
        word_set = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and suffix in word_set:
                    memo[word] = True
                    return True
                if prefix in word_set and dfs(suffix):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        return [word for word in words if dfs(word)]

=======
Suggestion 9

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        res = []

        def dfs(word: str, count: int) -> bool:
            if not word:
                return count > 1
            for i in range(len(words)):
                if words[i] != word and words[i] == word[:len(words[i])]:
                    if dfs(word[len(words[i]):], count + 1):
                        return True
            return False

        for i in range(len(words)):
            if dfs(words[i], 0):
                res.append(words[i])
        return res

=======
Suggestion 10

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        wordDict = set(words)
        def dfs(word: str, count: int) -> bool:
            if word in wordDict and count >= 1:
                return True
            for i in range(1, len(word)):
                if word[:i] in wordDict and dfs(word[i:], count + 1):
                    return True
            return False
        return [word for word in words if dfs(word, 0)]
