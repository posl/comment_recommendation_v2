Synthesizing 10/10 solutions

=======
Suggestion 1

def findSubstringInWraproundString(self, s: str) -> int:
        if not s: return 0
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
Suggestion 2

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        # count[i] is the maximum unique substring end with ith letter.
        # 0 - 'a', 1 - 'b', ..., 25 - 'z'.
        count = [0] * 26
        
        # store longest contiguous substring ends at current position.
        maxLengthCur = 0
        
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                maxLengthCur += 1
            else:
                maxLengthCur = 1
            index = ord(s[i]) - ord('a')
            count[index] = max(count[index], maxLengthCur)
        
        # Sum to get result
        return sum(count)

=======
Suggestion 3

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [1] * 26
        length = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                length += 1
            else:
                length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
        return sum(dp)

=======
Suggestion 4

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25:
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
        count = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i-1]) == 1) or (ord(s[i]) - ord(s[i-1]) == -25):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 6

def findSubstringInWraproundString(self, s: str) -> int:
        # dp[i] is the maximum unique substring end with ith letter.
        # We use set to avoid duplicate substrings.
        dp = [0] * 26
        #count: the maximum unique substring end with current letter.
        count = 0
        for i in range(len(s)):
            # If the current letter is not continu

=======
Suggestion 7

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*26
        dp[ord(s[0]) - ord('a')] = 1
        length = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                length += 1
            else:
                length = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
        return sum(dp)

=======
Suggestion 8

def findSubstringInWraproundString(self, s: str) -> int:
        # if length of s is 1, return 1
        if len(s) == 1:
            return 1
        # if length of s is 2, return 3 if s is "ab" or "bc" or "yz", otherwise return 2
        if len(s) == 2:
            if ord(s[1]) - ord(s[0]) == 1 or ord(s[1]) - ord(s[0]) == -25:
                return 3
            else:
                return 2
        # otherwise, create a dictionary to store the number of substrings ending with each letter
        # and return the sum of the values in the dictionary
        else:
            d = dict()
            for i in range(len(s)):
                if i == 0:
                    d[s[i]] = 1
                else:
                    if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i]) - ord(s[i-1]) == -25:
                        if s[i] in d:
                            d[s[i]] = max(d[s[i]], 1)
                        else:
                            d[s[i]] = 1
                        if s[i-1] in d:
                            d[s[i]] += d[s[i-1]]
                    else:
                        if s[i] in d:
                            d[s[i]] = max(d[s[i]], 1)
                        else:
                            d[s[i]] = 1
            return sum(d.values())

=======
Suggestion 9

def findSubstringInWraproundString(self, s: str) -> int:
        count = 0
        countDict = {}
        prev = None
        for i in range(len(s)):
            char = s[i]
            if prev:
                if (ord(char) - ord(prev) == 1) or (prev == 'z' and char == 'a'):
                    count += 1
                else:
                    count = 1
            else:
                count = 1
            prev = char
            countDict[char] = max(countDict.get(char, 0), count)
        return sum(countDict.values())

=======
Suggestion 10

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)
        
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        currMax = 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                currMax += 1
            else:
                currMax = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], currMax)
        
        return sum(dp)
