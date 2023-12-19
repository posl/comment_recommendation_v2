def findAllConcatenatedWordsInADict(words):
    def dfs(word, wordDict, memo):
        if word in memo: return memo[word]
        memo[word] = False
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and suffix in wordDict:
                memo[word] = True
                break
            if prefix in wordDict and dfs(suffix, wordDict, memo):
                memo[word] = True
                break
            if suffix in wordDict and dfs(prefix, wordDict, memo):
                memo[word] = True
                break
        return memo[word]
    
    memo = {}
    wordDict = set(words)
    res = []
    for word in words:
        if dfs(word, wordDict, memo):
            res.append(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
