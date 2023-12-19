def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    #Approach: Trie
    #Time Complexity: O(n * k^2)
    #Space Complexity: O(n * k^2)
    #where, n is the number of words and k is the length of each word
    
    class Node:
        def __init__(self):
            self.isEnd = False
            self.children = {}
            
    class Trie:
        def __init__(self):
            self.root = Node()
            
        def insert(self, word):
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.isEnd = True
            
        def search(self, word):
            curr = self.root
            for i in range(len(word)):
                char = word[i]
                if char not in curr.children:
                    return False
                curr = curr.children[char]
                if curr.isEnd:
                    if i == len(word) - 1:
                        return True
                    if self.search(word[i+1:]):
                        return True
            return False
    
    trie = Trie()
    for word in words:
        if word:
            trie.insert(word)
            
    ans = []
    for word in words:
        if word:
            if trie.search(word):
                ans.append(word)
    return ans

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()