def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    d = set()
    def check(word):
        if word in d:
            return True
        for i in range(1, len(word)):
            if word[:i] in d and check(word[i:]):
                return True
        return False
    res = []
    for word in words:
        if check(word):
            res.append(word)
        d.add(word)
    return res
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print("The arrays above should be [\"catsdogcats\",\"dogcatsdog\",\"ratcatdogcat\"] \
    and [\"catdog\"].")

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()