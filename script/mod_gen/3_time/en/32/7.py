def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    #Approach: Use a set to store all the words. For each word, check if it can be formed by concatenating two or more words from the set.
    #Time complexity: O(n^2)
    #Space complexity: O(n)
    words = set(words)
    def dfs(word):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                return True
            if prefix in words and dfs(suffix):
                return True
        return False
    
    result = []
    for word in words:
        if dfs(word):
            result.append(word)
            
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()