def findAllConcatenatedWordsInADict(words): #words: List[str]) -> List[str]:
    def check(word):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                memo[word] = True
                return True
            if prefix in words and check(suffix):
                memo[word] = True
                return True
        memo[word] = False
        return False
    words = set(words)
    memo = {}
    return [word for word in words if check(word)]
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
