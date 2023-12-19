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
    res = []
    words = set(words)
    for word in words:
        if len(word) == 0:
            continue
        dp = [False for _ in range(len(word) + 1)]
        dp[0] = True
        for i in range(1, len(word) + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if word[j:i] in words:
                    dp[i] = True
                    break
        if dp[-1]:
            res.append(word)
    return res

=======
Suggestion 3

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordSet, cache):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordSet and suffix in wordSet:
                cache[word] = True
                return True
            if prefix in wordSet and dfs(suffix, wordSet, cache):
                cache[word] = True
                return True
        cache[word] = False
        return False

    wordSet = set(words)
    cache = {}
    res = []
    for word in words:
        if dfs(word, wordSet, cache):
            res.append(word)
    return res

=======
Suggestion 4

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words = set(words)
    cache = {}
    def dfs(word):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                cache[word] = True
                return True
            if prefix in words and dfs(suffix):
                cache[word] = True
                return True
        cache[word] = False
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))

=======
Suggestion 5

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    if len(words) < 3:
        return []
    words.sort(key = len)
    word_set = set()
    ans = []
    for word in words:
        if word == "":
            continue
        if word in word_set:
            ans.append(word)
        for i in range(len(word)):
            if word[:i+1] in word_set and word[i+1:] != "" and word[i+1:] in word_set:
                ans.append(word)
                break
        word_set.add(word)
    return ans

=======
Suggestion 6

def findAllConcatenatedWordsInADict(words):
    words.sort(key=lambda x: len(x))
    print(words)
    result = []
    wordSet = set()
    for word in words:
        if wordBreak(word, wordSet):
            result.append(word)
        wordSet.add(word)
    return result

=======
Suggestion 7

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def helper(word, wordDict):
        if word in wordDict:
            return wordDict[word]
        for i in range(1, len(word)):
            if word[:i] in wordDict:
                if word[i:] in wordDict[word[:i]] or helper(word[i:], wordDict):
                    wordDict[word] = True
                    return True
        wordDict[word] = False
        return False

    wordDict = {}
    words.sort(key=len)
    res = []
    for word in words:
        if helper(word, wordDict):
            res.append(word)
    return res

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))

=======
Suggestion 8

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n)
    # where n is the number of words in the input list
    def dfs(word, wordset, cache):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordset and suffix in wordset:
                cache[word] = True
                return True
            if prefix in wordset and dfs(suffix, wordset, cache):
                cache[word] = True
                return True
        cache[word] = False
        return False
    
    wordset = set(words)
    cache = {}
    return [word for word in words if dfs(word, wordset, cache)]

=======
Suggestion 9

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Time Complexity: O(n^2 * m)
    # Space Complexity: O(n)
    # n is the length of words
    # m is the average length of each word
    word_set = set(words)
    cache = {}
    def helper(word):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                cache[word] = True
                return True
            if prefix in word_set and helper(suffix):
                cache[word] = True
                return True
        cache[word] = False
        return False
    result = []
    for word in words:
        if helper(word):
            result.append(word)
    return result

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))

=======
Suggestion 10

def findAllConcatenatedWordsInADict(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(word, start, count):
            if start == len(word) and count >= 2:
                return True
            for i in range(start, len(word)):
                if word[start:i+1] in wordSet and dfs(word, i+1, count+1):
                    return True
            return False
        wordSet = set(words)
        return [word for word in words if dfs(word, 0, 0)]

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
