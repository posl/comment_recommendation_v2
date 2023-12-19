Synthesizing 10/10 solutions

=======
Suggestion 1

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words = set(words)
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                return True
            if prefix in words and dfs(suffix):
                return True
            if suffix in words and dfs(prefix):
                return True
        return False

    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog","dogcat","catdogcat","catdogcatdogcat","catdogcatdogcatdogcat","catdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcat","catdogcatdogcatdogcatdogcatdogcatdogcat"]))
print("The arrays above should be [\"catsdog

=======
Suggestion 2

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def helper(word, wordSet, cache):
        if word in cache:
            return cache[word]
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet:
                if suffix in wordSet or helper(suffix, wordSet, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False
    
    wordSet = set(words)
    cache = {}
    res = []
    for word in words:
        if helper(word, wordSet, cache):
            res.append(word)
    return res

=======
Suggestion 3

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    wordSet = set(words)
    
    for word in words:
        wordSet.remove(word)
        if word:
            if dfs(word, wordSet, {}):
                res.append(word)
        wordSet.add(word)
    return res

=======
Suggestion 4

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    result = []
    wordDict = set()
    for word in words:
        if canForm(word, wordDict):
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
    result = []
    word_dict = set(words)
    for word in words:
        word_dict.remove(word)
        if isConcatenated(word, word_dict):
            result.append(word)
        word_dict.add(word)
    return result

=======
Suggestion 6

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    words = set(words)
    for word in words:
        words.remove(word)
        if isConcatenated(word, words):
            res.append(word)
        words.add(word)
    return res

=======
Suggestion 7

def findAllConcatenatedWordsInADict(words):
	"""
	:type words: List[str]
	:rtype: List[str]
	"""
	words = set(words)
	def dfs(word):
		for i in range(1, len(word)):
			prefix = word[:i]
			suffix = word[i:]
			if prefix in words and suffix in words:
				return True
			if prefix in words and dfs(suffix):
				return True
			if suffix in words and dfs(prefix):
				return True
		return False
	res = []
	for word in words:
		if dfs(word):
			res.append(word)
	return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))

=======
Suggestion 8

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    #Approach: Trie
    #Time Complexity: O(n * k^2)
    #Space Complexity: O(n * k^2)
    #where, n is the number of words and k is the length of each word
    
    class Node:
        def __init__(self):
            self.isEnd = False
            self.children = {}
            
    class Trie:
        def __init__(self):
            self.root = Node()
            
        def insert(self, word):
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.isEnd = True
            
        def search(self, word):
            curr = self.root
            for i in range(len(word)):
                char = word[i]
                if char not in curr.children:
                    return False
                curr = curr.children[char]
                if curr.isEnd:
                    if i == len(word) - 1:
                        return True
                    if self.search(word[i+1:]):
                        return True
            return False
    
    trie = Trie()
    for word in words:
        if word:
            trie.insert(word)
            
    ans = []
    for word in words:
        if word:
            if trie.search(word):
                ans.append(word)
    return ans

=======
Suggestion 9

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordSet, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet and suffix in wordSet:
                memo[word] = True
                return True
            if prefix in wordSet and dfs(suffix, wordSet, memo):
                memo[word] = True
                return True
        memo[word] = False
        return False

    wordSet = set(words)
    memo = {}
    ans = []
    for word in words:
        if dfs(word, wordSet, memo):
            ans.append(word)
    return ans

=======
Suggestion 10

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    words_set, res = set(), []
    for word in words:
        if wordBreak(word, words_set):
            res.append(word)
        words_set.add(word)
    return res
