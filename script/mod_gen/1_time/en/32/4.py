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

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()