def findAllConcatenatedWordsInADict(words):
	"""
	:type words: List[str]
	:rtype: List[str]
	"""
	words = set(words)
	def dfs(word):
		for i in range(1, len(word)):
			prefix = word[:i]
			suffix = word[i:]
			if prefix in words and suffix in words:
				return True
			if prefix in words and dfs(suffix):
				return True
			if suffix in words and dfs(prefix):
				return True
		return False
	res = []
	for word in words:
		if dfs(word):
			res.append(word)
	return res
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
