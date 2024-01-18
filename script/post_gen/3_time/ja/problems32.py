Synthesizing 10/10 solutions

=======
Suggestion 1

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        print(words)
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
        if len(words) <= 1:
            return []
        words.sort(key=len)
        #print(words)
        ans = []
        for i in range(len(words)):
            words_set = set(words[:i])
            #print(words_set)
            if self.isConcatenated(words[i], words_set):
                ans.append(words[i])
        return ans

=======
Suggestion 3

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def dfs(word, count):
            if word in memo:
                return memo[word]
            if word in words and count > 0:
                memo[word] = True
                return True
            for i in range(1, len(word)):
                if word[:i] in words and dfs(word[i:], count+1):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        memo = {}
        words.sort(key = lambda x: len(x))
        return [word for word in words if dfs(word, 0)]

=======
Suggestion 4

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def makeTrie(words):
            root = {}
            for word in words:
                node = root
                for c in word:
                    if c not in node:
                        node[c] = {}
                    node = node[c]
                node["#"] = "#"
            return root
        def search(word, root, start):
            node = root
            for i in range(start, len(word)):
                c = word[i]
                if c not in node:
                    return False
                node = node[c]
                if "#" in node:
                    if i == len(word) - 1:
                        return True
                    if search(word, root, i + 1):
                        return True
            return False
        root = makeTrie(words)
        return [word for word in words if search(word, root, 0)]

=======
Suggestion 5

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # 1. 先頭から順に、単語を1つずつ見ていく
        # 2. 単語の文字列を1文字ずつ、順に見ていく
        # 3. 単語の文字列を1文字ずつ、順に見ていく
        # 4. 単語の文字列を1文字ずつ、順に見ていく
        # 5. 単語の文字列を1文字ずつ、順に見ていく
        # 6. 単語の文字列を1文字ずつ、順に見ていく
        # 7. 単語の文字列を1文字ずつ、順に見ていく
        # 8. 単語の文字列を1文字ずつ、順に見ていく
        # 9. 単語の文字列を1文字ずつ、順に見ていく
        # 10. 単語の文字列を1文字ずつ、順に見ていく
        # 11. 単語の文字列を1文字ずつ、順に見ていく
        # 12. 単語の文字列を1文字ずつ、順に見ていく
        # 13. 単語の文字列を1文字ずつ、順に見ていく
        # 14. 単語の文字列を1文字ずつ、順に見ていく
        # 15. 単語の文字列を1文字ずつ、順に見ていく
        # 16. 単語の文字列を1文字ずつ、順に見ていく
        # 17. 単語の文字列を1文字ずつ、順に見ていく
        # 18. 単語の文字列を1文字ずつ、順に見ていく
        # 19. 単語の文字

=======
Suggestion 6

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def dfs(word: str) -> bool:
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in words and suffix in words:
                    memo[word] = True
                    return True
                if prefix in words and dfs(suffix):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        memo = {}
        words.sort(key=lambda x: len(x))
        ans = []
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans

=======
Suggestion 7

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
                if suffix in wordset and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]

        return [word for word in words if dfs(word)]

=======
Suggestion 8

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x: len(x))
        word_set = set()
        res = []

        def dfs(word):
            if not word:
                return True
            for i in range(1, len(word) + 1):
                if word[:i] in word_set:
                    if dfs(word[i:]):
                        return True
            return False

        for word in words:
            if dfs(word):
                res.append(word)
            word_set.add(word)

        return res

=======
Suggestion 9

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        def dfs(s, d):
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix, d):
                    return True
            return False

        d = set(words)
        res = []
        for word in words:
            d.remove(word)
            if dfs(word, d):
                res.append(word)
            d.add(word)
        return res

=======
Suggestion 10

def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        #wordsを昇順に並べ替える
        words.sort(key=lambda x: len(x))
        ans = []
        #wordsの中の単語が連結された単語かどうかを判定する
        def dfs(word, words):
            #wordsの中の単語を一つずつ取り出す
            for i in range(len(words)):
                #取り出した単語がwordに含まれていたら
                if words[i] in word:
                    #wordから取り出した単語を削除する
                    word = word.replace(words[i], "")
                    #wordが空になったらTrueを返す
                    if word == "":
                        return True
                    #wordが空にならなかったら再帰的にdfsを呼び出す
                    else:
                        return dfs(word, words)
            #wordに含まれていなかったらFalseを返す
            return False
        #wordsの中の単語を一つずつ取り出す
        for i in range(len(words)):
            #wordをwordsの中の単語で初期化する
            word = words[i]
            #wordが連結された単語ならansに追加する
            if dfs(word, words):
                ans.append(word)
        return ans
