Synthesizing 10/10 solutions

=======
Suggestion 1

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """

=======
Suggestion 2

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key = lambda x: len(x))
    wordSet = set()
    result = []
    for word in words:
        if wordBreak(word, wordSet):
            result.append(word)
        wordSet.add(word)
    return result

=======
Suggestion 3

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=lambda x: len(x))
    print(words)

    def dfs(word, d):
        if word in d:
            return d[word]
        for i in range(1, len(word)):
            if word[:i] in d and dfs(word[i:], d):
                d[word] = True
                return True
        d[word] = False
        return False

    res = []
    d = {}
    for word in words:
        if dfs(word, d):
            res.append(word)
    return res

=======
Suggestion 4

def findAllConcatenatedWordsInADict(words):
    words.sort(key=len)
    result = []
    wordDict = set()
    for word in words:
        if wordBreak(word, wordDict):
            result.append(word)
        wordDict.add(word)
    return result

=======
Suggestion 5

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, start, wordDict):
        if start == len(word):
            return True
        for i in range(start, len(word)):
            if word[start:i+1] in wordDict and dfs(word, i+1, wordDict):
                return True
        return False
    
    wordDict = set(words)
    res = []
    for word in words:
        wordDict.remove(word)
        if dfs(word, 0, wordDict):
            res.append(word)
        wordDict.add(word)
    return res

=======
Suggestion 6

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
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
            if suffix in word_set and dfs(prefix, word_set, memo):
                memo[word] = True
                break
        return memo[word]
    
    word_set = set(words)
    memo = {}
    return [word for word in words if dfs(word, word_set, memo)]

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","dog","catdog"]
print(findAllConcatenatedWordsInADict(words))

=======
Suggestion 7

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Solution 1 - 56 ms
    """
    wordDict = set(words)
    def isConcatenated(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and suffix in wordDict:
                return True
            if prefix in wordDict and isConcatenated(suffix):
                return True
        return False
    
    result = []
    for word in words:
        if isConcatenated(word):
            result.append(word)
    return result
    """
    # Solution 2 - 28 ms
    wordDict = set(words)
    def isConcatenated(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and (suffix in wordDict or isConcatenated(suffix)):
                return True
        return False
    
    result = []
    for word in words:
        if isConcatenated(word):
            result.append(word)
    return result

import collections

=======
Suggestion 8

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    res = []
    wordset = set()
    for word in words:
        if canForm(word, wordset):
            res.append(word)
        wordset.add(word)
    return res

=======
Suggestion 9

def problem(words):
    #words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    #words = ["cat","dog","catdog"]
    #words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","catdog"]
    #words = ["a","aa","aaa"]
    #words = ["a","b","ab","abc"]
    #words = ["a","ab","abc","abcd","abcde","abcdef","abcdefg","abcdefgh","abcdefghi","abcdefghij","abcdefghijk","abcdefghijkl","abcdefghijklm","nopqrstuvwxyz"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ab"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab","aba"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab","aba","abaa"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab","aba","abaa","abaaa"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab","aba","abaa","abaaa","abaaaa"]
    #words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab","aba","abaa","abaaa","abaaaa","abaaaaa"]
    #words = ["a","aa","aaa","aaaa","aaaaa

=======
Suggestion 10

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # create a trie
    trie = {}
    for word in words:
        node = trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = {}
    
    def dfs(word):
        node = trie
        for i, c in enumerate(word):
            if c not in node:
                return False
            node = node[c]
            if '$' in node and dfs(word[i+1:]):
                return True
        return '$' in node
    
    return [word for word in words if dfs(word)]
