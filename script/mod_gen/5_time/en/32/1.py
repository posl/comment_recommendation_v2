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

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()