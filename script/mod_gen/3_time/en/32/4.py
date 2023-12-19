def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # Space Complexity: O(n)
    # Runtime: 268 ms, faster than 93.20% of Python3 online submissions for Concatenated Words.
    # Memory Usage: 23.9 MB, less than 72.12% of Python3 online submissions for Concatenated Words.
    def dfs(word, word_set, cache):
        if word in cache:
            return cache[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                cache[word] = True
                return True
            if prefix in word_set and dfs(suffix, word_set, cache):
                cache[word] = True
                return True
        cache[word] = False
        return False
    word_set = set(words)
    cache = {}
    return [word for word in words if dfs(word, word_set, cache)]

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()