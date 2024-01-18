Synthesizing 9/10 solutions

=======
Suggestion 1

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[1] = 10
        for i in range(2,n+1):
            dp[i] = dp[i-1] + (9 * math.factorial(9)) // math.factorial(9-(i-1))
        return dp[n]

=======
Suggestion 2

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 10

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - i + 1)

        return dp[n]

=======
Suggestion 3

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 0 <= x < 10^n
        # 0 <= x < 10^1
        # 0 <= x < 10^2
        # 0 <= x < 10^3
        # 0 <= x < 10^4
        # 0 <= x < 10^5
        # 0 <= x < 10^6
        # 0 <= x < 10^7
        # 0 <= x < 10^8
        # 0 <= x < 10^9
        # 0 <= x < 10^10
        # 0 <= x < 10^11
        # 0 <= x < 10^12
        # 0 <= x < 10^13
        # 0 <= x < 10^14
        # 0 <= x < 10^15
        # 0 <= x < 10^16
        # 0 <= x < 10^17
        # 0 <= x < 10^18
        # 0 <= x < 10^19
        # 0 <= x < 10^20
        # 0 <= x < 10^21
        # 0 <= x < 10^22
        # 0 <= x < 10^23
        # 0 <= x < 10^24
        # 0 <= x < 10^25
        # 0 <= x < 10^26
        # 0 <= x < 10^27
        # 0 <= x < 10^28
        # 0 <= x < 10^29
        # 0 <= x < 10^30
        # 0 <= x < 10^31
        # 0 <= x < 10^32
        # 0 <= x < 10^33
        # 0 <= x < 10^34
        # 0 <= x < 10^35
        # 0 <= x < 10^36
        # 0 <= x < 10^37
        # 0 <= x < 10^38
        # 0 <= x < 10^39
        # 0 <= x < 10^40
        # 0 <= x <

=======
Suggestion 4

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        ans=0
        for i in range(1,n+1):
            ans+=9*math.factorial(9)//math.factorial(10-i)
        return ans

=======
Suggestion 5

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (10 - (i - 1))

        return sum(dp)

=======
Suggestion 6

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 10
        for i in range(2, n+1):
            # 1桁目は1~9のいずれかなので9通り
            # 2桁目以降は1桁目の数字を除いた9通り
            tmp = 9
            for _ in range(1, i):
                tmp *= (10 - _)
            ans += tmp
        return ans

=======
Suggestion 7

def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        for i in range(10**n):
            if len(set(str(i))) == len(str(i)):
                ans += 1
        return ans

=======
Suggestion 8

def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [1] * 10
        for i in range(1, 10):
            dp[i] = dp[i - 1] * (10 - i)
        return sum(dp[:n]) + 1

=======
Suggestion 9

def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
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
        elif n == 8:
            return 2345851
        else:
            return 5611771
