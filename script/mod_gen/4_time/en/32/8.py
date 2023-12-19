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
