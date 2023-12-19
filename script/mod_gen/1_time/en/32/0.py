def findAllConcatenatedWordsInADict(words):
    ans = []
    words.sort(key=len)
    wordDict = set()
    for word in words:
        if word == "":
            continue
        if isConcatenated(word, wordDict):
            ans.append(word)
        wordDict.add(word)
    return ans

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()