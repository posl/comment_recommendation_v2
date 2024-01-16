Synthesizing 10/10 solutions

=======
Suggestion 1

def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i] == 'a'):
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')],count)
        return sum(dp)

=======
Suggestion 2

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1]) == 1 or (s[i-1] == 'z' and s[i] == 'a'):
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], count)
        return sum(dp)

=======
Suggestion 3

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        char_dict = {}
        for i in range(26):
            char_dict[chr(ord('a') + i)] = 0
        char_dict[s[0]] = 1
        max_len = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25:
                max_len += 1
            else:
                max_len = 1
            char_dict[s[i]] = max(char_dict[s[i]], max_len)
        return sum(char_dict.values())

=======
Suggestion 4

def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 5

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        l = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                l += 1
            else:
                l = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], l)
        return sum(dp)

=======
Suggestion 6

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or (ord(s[i-1]) - ord(s[i]) == 25):
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], count)
        return sum(dp)

=======
Suggestion 7

def findSubstringInWraproundString(self, s: str) -> int:
        # dp[i] - the max unique substring end with ith letter.
        # We use set to avoid duplicate substrings.
        # We can add all substring end with ith letter.
        # For example: "abcd", the substrings end with 'd' are "abcd","bcd","cd","d",
        # Then we add "abcd" and "d" to our result set.
        dp = [0] * 26
        #count consecutive substring end with ith letter
        #dp[i] = 1 means letter 'a'+i occurs only once
        maxLength = 1
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                maxLength += 1
            else:
                maxLength = 1
            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], maxLength)
        return sum(dp)

=======
Suggestion 8

def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dp = [1] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i-1]) == 1) or (ord(s[i-1]) - ord(s[i]) == 25):
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        print(dp)
        return sum(dp)

=======
Suggestion 9

def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i - 1]) - ord(s[i]) == 25):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 10

def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [1] * 26
        start = ord(s[0])
        length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - start == length or (ord(s[i]) - start == -25 and length == 1):
                length += 1
            else:
                length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
            start = ord(s[i])
        return sum(dp)
