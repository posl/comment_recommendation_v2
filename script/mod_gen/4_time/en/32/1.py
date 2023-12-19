def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    res = []
    words = set(words)
    for word in words:
        if len(word) == 0:
            continue
        dp = [False for _ in range(len(word) + 1)]
        dp[0] = True
        for i in range(1, len(word) + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if word[j:i] in words:
                    dp[i] = True
                    break
        if dp[-1]:
            res.append(word)
    return res

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()