Synthesizing 10/10 solutions

=======
Suggestion 1

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        
        for i in range(4, n + 1):
            dp[i] = max(3 * dp[i - 3], 2 * dp[i - 2])
            
        return dp[n]

=======
Suggestion 2

def integerBreak(self, n: int) -> int:
        # 2の時は1*1
        if n == 2:
            return 1
        # 3の時は1*2
        if n == 3:
            return 2
        # それ以外の時は3の積を求める
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

=======
Suggestion 3

def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        else:
            if n % 3 == 0:
                return 3 ** (n // 3)
            elif n % 3 == 1:
                return 3 ** (n // 3 - 1) * 4
            else:
                return 3 ** (n // 3) * 2

=======
Suggestion 4

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product

=======
Suggestion 5

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        ans = 1
        while n > 4:
            n -= 3
            ans *= 3
        
        return ans * n

=======
Suggestion 6

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        ans = 0
        for i in range(2, n + 1):
            x = n // i
            y = n % i
            ans = max(ans, pow(x, i - y) * pow(x + 1, y))
        return ans

=======
Suggestion 7

class Solution:
    def integerBreak(self, n: int) -> int:
        # 2以上の整数を最大2つの正の整数の和に分解し、その積を最大化する
        # 2の場合は1*1=1
        # 3の場合は1*2=2
        # 4の場合は2*2=4
        # 5の場合は3*2=6
        # 6の場合は3*3=9
        # 7の場合は3*4=12
        # 8の場合は3*3*2=18
        # 9の場合は3*3*3=27
        # 10の場合は3*3*4=36
        # 11の場合は3*3*3*2=54
        # 12の場合は3*3*3*3=81
        # 13の場合は3*3*3*4=108
        # 14の場合は3*3*3*3*2=162
        # 15の場合は3*3*3*3*3=243
        # 16の場合は3*3*3*3*4=324
        # 17の場合は3*3*3*3*3*2=486
        # 18の場合は3*3*3*3*3*3=729
        # 19の場合は3*3*3*3*3*4=972
        # 20の場合は3*3*3*3*3*3*2=1458
        # 21の場合は3*3*3*3*3*3*3=2187
        # 22の場合は3*3*3*3*3*3*4=2916
        # 23の場合は3*3*3*3*3*3*3*2=4374
        # 24の場合は3*3*3*3*3*3*3*3=6561
        # 25の場合は3*3*3*3*3*3*3*4=

=======
Suggestion 8

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return ans * n

=======
Suggestion 9

def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        else:
            ans = 1
            while n > 4:
                ans *= 3
                n -= 3
            ans *= n
            return ans

=======
Suggestion 10

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        elif n == 5:
            return 6
        elif n == 6:
            return 9
        else:
            if n % 3 == 0:
                return 3 ** (n // 3)
            elif n % 3 == 1:
                return 3 ** (n // 3 - 1) * 4
            else:
                return 3 ** (n // 3) * 2
