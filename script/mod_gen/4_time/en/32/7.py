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

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()