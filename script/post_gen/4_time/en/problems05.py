Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
                length += 1
            else:
                length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
        return sum(dp)

=======
Suggestion 2

def findSubstringInWraproundString(self, s: str) -> int:
        # Solution 1 - 40 ms
        """
        if len(s) == 0: return 0
        dp = [1] * 26
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == "z" and s[i] == "a"):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord("a")] = max(dp[ord(s[i]) - ord("a")], count)
        return sum(dp)
        """
        # Solution 2 - 20 ms
        if len(s) == 0: return 0
        dp = [1] * 26
        count = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord("a")] = max(dp[ord(s[i]) - ord("a")], count)
        return sum(dp)

=======
Suggestion 3

def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0]*26
        count = 0
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 4

def findSubstringInWraproundString(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        # 从左往右扫描, 以当前字符结尾的最长连续子串的长度
        # dp[i] 表示以字符 i 结尾的最长连续子串的长度
        dp = [0] * 26
        # 以当前字符结尾的最长连续子串的长度
        cur = 1
        dp[ord(s[0]) - ord('a')] = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i - 1]) - ord(s[i]) == 25 and cur == 1):
                cur += 1
            else:
                cur = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], cur)
        return sum(dp)

=======
Suggestion 5

def findSubstringInWraproundString(self, s: str) -> int:
        #Approach: Dynamic Programming
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        
        if not s:
            return 0
        
        dp = [0] * 26
        
        currLen = 1
        dp[ord(s[0]) - ord('a')] = 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
                currLen += 1
            else:
                currLen = 1
                
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], currLen)
            
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
            if ord(s[i])-ord(s[i-1]) == 1 or ord(s[i-1])-ord(s[i]) == 25:
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], count)
        return sum(dp)

=======
Suggestion 7

def findSubstringInWraproundString(self, s: str) -> int:
        # Solution 1 - 44 ms
        """
        if not s:
            return 0

        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)
        """
        # Solution 2 - 16 ms
        if not s:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 8

def findSubstringInWraproundString(self, s: str) -> int:
        # dp[i] is the maximum unique substring end with ith letter.
        # We use set to avoid duplicate substrings.
        # dp[i] = dp[i-1] + 1 if s[i] - s[i-1] is not in substring set.
        # We just need to loop through the string and sum up all dp[i].
        # To get substring ending with ith letter, we need to multiply
        # (length of substring end with previous letter + 1) * 1
        # Example:
        # abc, when we reach c, we have abc, bc, c
        # dp[0] = set([a]), res += 1 * 1 = 1
        # dp[1] = set([ab, b]), res += 2 * 2 = 4
        # dp[2] = set([abc, bc, c]), res += 3 * 3 = 9
        # total = 14
        dp = [0] * 26
        # Length of substring end at current position.
        length = 0
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            if i > 0 and ord(s[i-1]) != (cur - 1) % 26 + ord('a'):
                length = 0
            length += 1
            dp[cur] = max(dp[cur], length)
        return sum(dp)

=======
Suggestion 9

def findSubstringInWraproundString(self, s: str) -> int:
        if not s: return 0
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1,len(s)):
            if (ord(s[i])-ord(s[i-1]))%26 == 1:
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')],count)
        return sum(dp)
