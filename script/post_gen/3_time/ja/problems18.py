Synthesizing 10/10 solutions

=======
Suggestion 1

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        else:
            ans = 91
            for i in range(3, n+1):
                ans += self.combination(i)
            return ans

=======
Suggestion 2

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # dp[i] := 各桁が異なる数字で構成されていて、0 <= x < 10^i を満たす整数 x の個数
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            # dp[i] = dp[i-1] + (dp[i-1] - dp[i-2]) * (10 - i + 1)
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - i + 1)

        return dp[n]

=======
Suggestion 3

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
                tmp = 9
                for j in range(1,i):
                    tmp *= (10-j)
                ans += tmp
            return ans

=======
Suggestion 4

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            ans = 10
            for i in range(2, n+1):
                tmp = 9
                for j in range(9, 9-i+1, -1):
                    tmp *= j
                ans += tmp
            return ans

=======
Suggestion 5

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        for i in range(2, n + 1):
            tmp = 9
            for j in range(1, i):
                tmp *= (10 - j)
            ans += tmp
        return ans

=======
Suggestion 6

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n > 10:
            n = 10
        dp = [0] * (n+1)
        dp[1] = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1] * (10 - i + 1)
        return sum(dp)

=======
Suggestion 7

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n+1):
            dp[i] = dp[i-1] + (dp[i-1] - dp[i-2]) * (10 - (i - 1))
            
        return dp[n]

=======
Suggestion 8

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        ans = 10
        for i in range(2, n + 1):
            tmp = 9
            for j in range(i - 1):
                tmp *= (9 - j)
            ans += tmp
        return ans

=======
Suggestion 9

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (9 - i + 2)

        return sum(dp)

=======
Suggestion 10

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        for i in range(2, n + 1):
            tmp = 9
            for j in range(9, 9 - i + 1, -1):
                tmp *= j
            ans += tmp

        return ans
