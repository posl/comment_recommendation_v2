def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    if len(words) < 3:
        return []
    words.sort(key = len)
    word_set = set()
    ans = []
    for word in words:
        if word == "":
            continue
        if word in word_set:
            ans.append(word)
        for i in range(len(word)):
            if word[:i+1] in word_set and word[i+1:] != "" and word[i+1:] in word_set:
                ans.append(word)
                break
        word_set.add(word)
    return ans

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()