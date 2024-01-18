Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + self.count(i)
        return dp[n]

=======
Suggestion 2

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        res = 10
        for i in range(2, n+1):
            tmp = 9
            for j in range(9, 9-i+1, -1):
                tmp *= j
            res += tmp
        return res

=======
Suggestion 3

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 9
        for i in range(2, n+1):
            dp[i] = dp[i-1] * (11 - i)
        return sum(dp)

=======
Suggestion 4

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 9
        for i in range(2, n+1):
            dp[i] = dp[i-1] * (10-i+1)
        
        return sum(dp)

=======
Suggestion 5

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        cnt = 9
        for i in range(9, 10-n, -1):
            cnt *= i
        return cnt + self.countNumbersWithUniqueDigits(n-1)

=======
Suggestion 6

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        else:
            ans = 91
            for i in range(3,n+1):
                ans += 9*9*10**(i-2)
            return ans

=======
Suggestion 7

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        def dfs(index, used, num, limit):
            if index == limit:
                return 1
            
            ans = 0
            for i in range(10):
                if i == 0 and index == 0:
                    continue
                if used >> i & 1:
                    continue
                if i == num:
                    continue
                ans += dfs(index + 1, used | 1 << i, i, limit)
            return ans
        
        ans = 0
        for i in range(1, n + 1):
            ans += dfs(0, 0, -1, i)
        return ans

=======
Suggestion 8

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n > 10:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1] + (dp[i-1] - dp[i-2]) * (10 - (i-1))
        return dp[n]

=======
Suggestion 9

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 0 <= x < 10^n
        # 0 <= n <= 8
        # 1 <= x <= 10^n - 1
        # 1 <= n <= 8
        # 1 <= x <= 10^n - 1
        # 1 <= x <= 10^n - 1
        #
