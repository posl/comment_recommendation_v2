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

if __name__ == '__main__':
    words = input().split()
    a = findAllConcatenatedWordsInADict(words)
    print(a)