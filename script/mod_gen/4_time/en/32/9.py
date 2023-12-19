def findAllConcatenatedWordsInADict(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(word, start, count):
            if start == len(word) and count >= 2:
                return True
            for i in range(start, len(word)):
                if word[start:i+1] in wordSet and dfs(word, i+1, count+1):
                    return True
            return False
        wordSet = set(words)
        return [word for word in words if dfs(word, 0, 0)]
print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
