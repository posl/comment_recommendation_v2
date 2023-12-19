def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=lambda x: len(x))
    print(words)
    def dfs(word, d):
        if word in d:
            return d[word]
        for i in range(1, len(word)):
            if word[:i] in d and dfs(word[i:], d):
                d[word] = True
                return True
        d[word] = False
        return False
    res = []
    d = {}
    for word in words:
        if dfs(word, d):
            res.append(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()