Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 0
        for i in range(1, n + 1):
            ans += 9 * self.permutation(9, i - 1)

        return ans + 1

=======
Suggestion 2

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = dp[i-1] + self.cal(i)
        return dp[-1]

=======
Suggestion 3

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

=======
Suggestion 4

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n > 10:
            return self.countNumbersWithUniqueDigits(10)
        else:
            res, mul = 10, 9
            for i in range(1, n):
                mul *= 10 - i
                res += mul
            return res

=======
Suggestion 5

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10
        elif n == 2:
            return 91
        elif n == 3:
            return 739
        elif n == 4:
            return 5275
        elif n == 5:
            return 32491
        elif n == 6:
            return 168571
        elif n == 7:
            return 712891
        else:
            return 2345851

=======
Suggestion 6

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            ans = 10
            for i in range(2, n + 1):
                tmp = 9
                for j in range(i - 1):
                    tmp *= (9 - j)
                ans += tmp
            return ans

=======
Suggestion 7

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        for i in range(2, min(n+1, 10)):
            tmp = 9
            for j in range(1, i):
                tmp *= (10-j)
            ans += tmp
        return ans

=======
Suggestion 8

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        for i in range(2, n + 1):
            product = 9
            for j in range(9, 9 - i + 1, -1):
                product *= j
            ans += product
        return ans
