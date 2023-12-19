def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    result = []
    def check(word):
        if not word:
            return True
        for i in range(1, len(word) + 1):
            if word[:i] in words and check(word[i:]):
                return True
        return False
    for word in words:
        words.remove(word)
        if check(word):
            result.append(word)
        words.append(word)
    return result
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(findAllConcatenatedWordsInADict(["cat","dog","catdog"]))
print(findAllConcatenatedWordsInADict([""]))
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","catsdogcatsdog"]))
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","catsdogcatsdog","catsdogcatsdogcats"]))
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","catsdogcatsdog","catsdogc
