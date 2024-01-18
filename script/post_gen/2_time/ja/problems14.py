Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        else:
            return 3 ** (n // 3) * 2

=======
Suggestion 2

def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n + 1):
            dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
        return dp[n]

=======
Suggestion 3

def integerBreak(self, n: int) -> int:
        # 2,3,4は特別扱い
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        
        # 5以降は3を優先して足す
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans

=======
Suggestion 4

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        count = 0
        while n > 4:
            count += 1
            n -= 3
            
        return 3 ** count * n

=======
Suggestion 5

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        ans *= n
        return ans

=======
Suggestion 6

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        res *= n
        return res

=======
Suggestion 7

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        a = n // 3
        b = n % 3
        
        if b == 0:
            return 3 ** a
        elif b == 1:
            return 3 ** (a - 1) * 4
        else:
            return 3 ** a * 2

=======
Suggestion 8

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        ans = 1
        while n > 4:
            n -= 3
            ans *= 3
        
        ans *= n
        
        return ans
