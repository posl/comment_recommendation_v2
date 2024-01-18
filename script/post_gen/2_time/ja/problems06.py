Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            umin = min(u2, u3, u5)
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
Suggestion 2

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
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2 = i3 = i5 = 0
        while len(dp) < n:
            ugly2 = dp[i2] * 2
            ugly3 = dp[i3] * 3
            ugly5 = dp[i5] * 5
            ugly = min(ugly2, ugly3, ugly5)
            if ugly == ugly2:
                i2 += 1
            if ugly == ugly3:
                i3 += 1
            if ugly == ugly5:
                i5 += 1
            dp.append(ugly)
        return dp[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > len(ugly):
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2: i2 += 1
            if umin == u3: i3 += 1
            if umin == u5: i5 += 1
            ugly.append(umin)
        return ugly[-1]

=======
Suggestion 5

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
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[n - 1]

=======
Suggestion 7

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 2,3,5 の積で作られる ugly number は ugly number である
        # 2,3,5 の積で作られる ugly number しか ugly number にならない
        # 2,3,5 の積で作られる ugly number は昇順に並んでいる
        # 2,3,5 の積で作られる ugly number は 1 から始まる
        # 2,3,5 の積で作られる ugly number は 1690 個まで存在する
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number である
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number しかない
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number で昇順に並んでいる
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number は 1 から始まる
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number は 1690 個まで存在する
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number は 2,3,5 の積で作られる ugly number である
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number は 2,3,5 の積で作られる ugly number しかない
        # 2,3,5 の積で作られる ugly number は 2,3,5 の倍数の ugly number は

=======
Suggestion 8

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
