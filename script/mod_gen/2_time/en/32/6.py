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

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()