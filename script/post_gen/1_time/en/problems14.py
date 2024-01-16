Synthesizing 10/10 solutions

=======
Suggestion 1

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        if n % 3 == 0:
            return 3**(n//3)
        elif n % 3 == 1:
            return 3**(n//3 - 1) * 4
        elif n % 3 == 2:
            return 3**(n//3) * 2

=======
Suggestion 2

def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [0, 1, 2, 3] + [0] * (n - 3)
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)
        return dp[n]

=======
Suggestion 3

def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*dp[i-j],j*(i-j))
        return dp[n]

=======
Suggestion 4

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3: 
            return 2
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 3**(n//3 - 1) * 4
        return 3**(n//3) * 2

=======
Suggestion 5

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],max(j * dp[i-j],j * (i-j)))
        return dp[n]

=======
Suggestion 6

def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n-1
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product*n

=======
Suggestion 7

def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)
        return dp[n]

=======
Suggestion 8

def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        return result * n

=======
Suggestion 9

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        return dp[n]

=======
Suggestion 10

def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*max(i-j,dp[i-j]))
        return dp[n]
