Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def findAllConcatenatedWordsInADict(words): #words: List[str]) -> List[str]:
    def check(word):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                memo[word] = True
                return True
            if prefix in words and check(suffix):
                memo[word] = True
                return True
        memo[word] = False
        return False
    words = set(words)
    memo = {}
    return [word for word in words if check(word)]


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))

=======
Suggestion 3

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordDict):
        if word in wordDict:
            return wordDict[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and wordDict[prefix] and dfs(suffix, wordDict):
                wordDict[word] = True
                return True
        wordDict[word] = False
        return False
    
    wordDict = {}
    for word in words:
        wordDict[word] = True
    res = []
    for word in words:
        wordDict[word] = False
        if dfs(word, wordDict):
            res.append(word)
    return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","dog","catdog"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))

=======
Suggestion 4

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

=======
Suggestion 5

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Sort the words by length
    words.sort(key=lambda x: len(x))
    # Define a set to store the words
    word_set = set()
    # Define a list to store the concatenated words
    concatenated_words = []
    # Iterate through the words
    for word in words:
        # Check if the word is a concatenated word
        if is_concatenated_word(word, word_set):
            # Add the word to the concatenated words list
            concatenated_words.append(word)
        # Add the word to the set
        word_set.add(word)
    # Return the concatenated words
    return concatenated_words

=======
Suggestion 6

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    #create a set of all the words
    words_set = set(words)
    #create a list of all the words
    words_list = list(words)
    #create a list for the concatenated words
    concatenated_words = []
    #loop through the list of words
    for word in words_list:
        #remove the word from the set
        words_set.remove(word)
        #if the word is in the set
        if isInSet(word, words_set):
            #add the word to the concatenated_words list
            concatenated_words.append(word)
        #add the word back to the set
        words_set.add(word)
    #return the concatenated_words list
    return concatenated_words

=======
Suggestion 7

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    wordDict = set(words)
    def dfs(word):
        for i in range(1,len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict and suffix in wordDict:
                return True
            if prefix in wordDict and dfs(suffix):
                return True
            if suffix in wordDict and dfs(prefix):
                return True
        return False
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res

=======
Suggestion 8

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    words.sort(key=len)
    wordDict = set()
    result = []
    for word in words:
        if wordBreak(word, wordDict):
            result.append(word)
        wordDict.add(word)
    return result

=======
Suggestion 9

def findAllConcatenatedWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    wordSet = set(words)
    concatWords = []
    for word in words:
        wordSet.remove(word)
        if isConcatWord(word, wordSet):
            concatWords.append(word)
        wordSet.add(word)
    return concatWords

=======
Suggestion 10

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    def dfs(word, wordDict, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordDict:
                if suffix in wordDict or dfs(suffix, wordDict, memo):
                    memo[word] = True
                    return True
        memo[word] = False
        return False

    wordDict = set(words)
    memo = {}
    return [word for word in words if dfs(word, wordDict, memo)]
