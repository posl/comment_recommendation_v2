Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

=======
Suggestion 2

def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            dp.append(min(2 * dp[p2], 3 * dp[p3], 5 * dp[p5]))
            if dp[i] == 2 * dp[p2]:
                p2 += 1
            if dp[i] == 3 * dp[p3]:
                p3 += 1
            if dp[i] == 5 * dp[p5]:
                p5 += 1
        return dp[-1]

=======
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        for l in range(1, n):
            ugly[l] = min(next2, next3, next5)
            if ugly[l] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[l] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[l] == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        return ugly[-1]

=======
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

=======
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2 = 2
        next3 = 3
        next5 = 5
        
        for l in range(1, n):
            ugly[l] = min(next2, next3, next5)
            if ugly[l] == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if ugly[l] == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if ugly[l] == next5:
                i5 += 1
                next5 = ugly[i5] * 5
        
        return ugly[-1]
