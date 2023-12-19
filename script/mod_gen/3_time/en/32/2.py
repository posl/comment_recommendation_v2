def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # where n is the number of words in the list
    # Approach: Dynamic Programming
    # We can use DP to solve this problem.
    # We first sort the input by length of each word.
    # Then we use a hash set to store all the words we have seen so far.
    # Iterate through each word, and check if it can be formed by the words we have seen so far.
    # To do this, we iterate through each character in the word, and check if the substring before the current character is in the hash set and if the substring after the current character is in the hash set.
    # If both are true, we can form the current word by concatenating the two substrings.
    # If we can form the current word, we add it to the result.
    # Finally, we return the result.
    if not words:
        return []
    words.sort(key=len)
    word_set = set()
    result = []
    for word in words:
        if wordBreak(word, word_set):
            result.append(word)
        word_set.add(word)
    return result

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()