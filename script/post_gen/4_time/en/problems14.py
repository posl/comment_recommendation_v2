Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n==3:
            return 2
        if n%3 == 0:
            return 3**(n//3)
        if n%3 == 1:
            return 3**(n//3-1)*4
        if n%3 == 2:
            return 3**(n//3)*2

=======
Suggestion 2

def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4,n+1):
            dp[i] = max(dp[i-2]*2, dp[i-3]*3)
        return dp[n]

=======
Suggestion 3

def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        if n==5:
            return 6
        if n==6:
            return 9
        return 3*self.integerBreak(n-3)

=======
Suggestion 4

def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3: 
            return 2
        if n % 3 == 0:
            return pow(3, n//3)
        if n % 3 == 1:
            return 4*pow(3, (n-4)//3)
        if n % 3 == 2:
            return 2*pow(3, (n-2)//3)

=======
Suggestion 5

def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        if n == 4:
            return n
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res

=======
Suggestion 6

def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 4
        else:
            return 3*self.integerBreak(n-3)

=======
Suggestion 7

class Solution:
    def integerBreak(self, n: int) -> int:
        #if n == 2:
        #    return 1
        #if n == 3:
        #    return 2
        #if n == 4:
        #    return 4
        #if n == 5:
        #    return 6
        #if n == 6:
        #    return 9
        #if n == 7:
        #    return 12
        #if n == 8:
        #    return 18
        #if n == 9:
        #    return 27
        #if n == 10:
        #    return 36
        #if n == 11:
        #    return 54
        #if n == 12:
        #    return 81
        #if n == 13:
        #    return 108
        #if n == 14:
        #    return 162
        #if n == 15:
        #    return 243
        #if n == 16:
        #    return 324
        #if n == 17:
        #    return 486
        #if n == 18:
        #    return 729
        #if n == 19:
        #    return 972
        #if n == 20:
        #    return 1458
        #if n == 21:
        #    return 2187
        #if n == 22:
        #    return 2916
        #if n == 23:
        #    return 4374
        #if n == 24:
        #    return 6561
        #if n == 25:
        #    return 8748
        #if n == 26:
        #    return 13122
        #if n == 27:
        #    return 19683
        #if n == 28:
        #    return 26244
        #if n == 29:
        #    return 39366
        #if n == 30:
        #    return 59049
        #if n == 31:
        #    return 78732
        #if n == 32:
        #    return 118098
        #if n == 33:
        #    return 177147
        #if n ==

=======
Suggestion 8

def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j*max(i-j,dp[i-j]))
        return dp[n]

=======
Suggestion 9

def integerBreak(self, n: int) -> int:
        if n<4:
            return n-1
        dp=[0,0,1,2,4,6,9]
        for i in range(7,n+1):
            dp.append(3*dp[i-3])
        return dp[n]
