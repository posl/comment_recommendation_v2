def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # create a trie
    trie = {}
    for word in words:
        node = trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = {}
    
    def dfs(word):
        node = trie
        for i, c in enumerate(word):
            if c not in node:
                return False
            node = node[c]
            if '$' in node and dfs(word[i+1:]):
                return True
        return '$' in node
    
    return [word for word in words if dfs(word)]

if __name__ == '__main__':
    findAllConcatenatedWordsInADict()