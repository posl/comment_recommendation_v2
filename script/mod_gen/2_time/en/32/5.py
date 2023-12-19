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
