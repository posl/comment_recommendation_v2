Synthesizing 10/10 solutions

=======
Suggestion 1

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        # dp[i] = max length of substring ends at i
        dp = [0] * len(s)
        dp[0] = 1
        # count[i] = max number of unique substrings ends at i
        count = [0] * len(s)
        count[0] = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (ord(s[i]) == 97 and ord(s[i - 1]) == 122):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            count[i] = max(count[i - 1], dp[i])
        return sum(count)

=======
Suggestion 2

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        count = [0]*26
        dp = [0]*len(s)
        dp[0] = 1
        count[ord(s[0])-ord('a')] = 1
        for i in range(1, len(s)):
            if (ord(s[i])-ord(s[i-1]))%26 == 1:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1
            count[ord(s[i])-ord('a')] = max(count[ord(s[i])-ord('a')], dp[i])
        return sum(count)

=======
Suggestion 3

def findSubstringInWraproundString(self, s: str) -> int:
        # 1. define a map to store the longest substring ends at that character
        # 2. loop the string, update map
        # 3. sum all values in map
        # 4. return sum
        # Time: O(n), Space: O(1)
        if not s:
            return 0
        dp = [0] * 26
        count = 1
        dp[ord(s[0]) - ord('a')] = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 4

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        cnt = [0]*26
        cur = 1
        cnt[ord(s[0])-ord('a')] = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1])+1 or (ord(s[i-1]) == ord('z') and ord(s[i]) == ord('a')):
                cur += 1
            else:
                cur = 1
            cnt[ord(s[i])-ord('a')] = max(cnt[ord(s[i])-ord('a')], cur)
        return sum(cnt)

=======
Suggestion 5

def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0]*26
        l = 0
        for i in range(len(s)):
            if i>0 and ord(s[i])-ord(s[i-1]) not in [1, -25]:
                l = 0
            l += 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], l)
        return sum(dp)

=======
Suggestion 6

def findSubstringInWraproundString(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [1 for _ in range(n)]
        d = {}
        d[s[0]] = 1
        for i in range(1, n):
            if s[i - 1] + s[i] in "abcdefghijklmnopqrstuvwxyza":
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            if s[i] in d:
                d[s[i]] = max(d[s[i]], dp[i])
            else:
                d[s[i]] = dp[i]
        return sum(d.values())

=======
Suggestion 7

def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        d = [0] * 26
        d[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'):
                count += 1
            else:
                count = 1
            d[ord(s[i]) - ord('a')] = max(d[ord(s[i]) - ord('a')], count)
        return sum(d)

=======
Suggestion 8

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 9

def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * 26
        dp[ord(s[0]) - ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or (ord(s[i]) == ord('a') and ord(s[i-1]) == ord('z')):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)

=======
Suggestion 10

def findSubstringInWraproundString(self, s: str) -> int:
        if not s: return 0
        # 1. find the longest substring for each character
        # 2. sum up the longest substring for each character
        # 3. return the sum
        dp = [0]*26
        dp[ord(s[0])-ord('a')] = 1
        count = 1
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1]) == 1 or ord(s[i])-ord(s[i-1]) == -25:
                count += 1
            else:
                count = 1
            dp[ord(s[i])-ord('a')] = max(dp[ord(s[i])-ord('a')], count)
        return sum(dp)
