Synthesizing 10/10 solutions

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
        ugly = [1]
        i2 = i3 = i5 = 0
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
Suggestion 3

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > len(ugly):
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            umin = min(u2, u3, u5)
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2 = i3 = i5 = 0
        for i in range(n - 1):
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
            if ugly[-1] == ugly[i2] * 2:
                i2 += 1
            if ugly[-1] == ugly[i3] * 3:
                i3 += 1
            if ugly[-1] == ugly[i5] * 5:
                i5 += 1
        return ugly[-1]

=======
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            min_ugly = min(u2, u3, u5)
            if min_ugly == u2:
                i2 += 1
            if min_ugly == u3:
                i3 += 1
            if min_ugly == u5:
                i5 += 1
            ugly.append(min_ugly)
        return ugly[-1]

=======
Suggestion 6

def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
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
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
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
Suggestion 8

def nthUglyNumber(self, n: int) -> int:
        #2,3,5の倍数を作成していく
        #2,3,5の倍数の中で最小の値を取得する
        #最小の値を取得したら2,3,5の倍数のリストからその値を削除する
        #n回繰り返す
        #最後に取得した値が答え

        two = [2]
        three = [3]
        five = [5]
        result = [1]
        for i in range(n):
            min_val = min(two[0],three[0],five[0])
            result.append(min_val)
            if min_val == two[0]:
                two.pop(0)
                two.append(min_val * 2)
                three.append(min_val * 3)
                five.append(min_val * 5)
            elif min_val == three[0]:
                three.pop(0)
                three.append(min_val * 3)
                five.append(min_val * 5)
            else:
                five.pop(0)
                five.append(min_val * 5)
        return result[n-1]

=======
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
        # 1は ugly number なので、1からスタートする
        ugly = [1]

        # 2, 3, 5 の倍数の ugly number を作っていく
        # それぞれの倍数の ugly number が入っているインデックス
        i2 = 0
        i3 = 0
        i5 = 0

        while len(ugly) < n:
            # 2, 3, 5 の倍数の中で最小の ugly number を計算する
            # 例えば、i2 は 2 の倍数の ugly number のうち、
            # ugly[i2] 以上の最小の ugly number が入っているインデックス
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5
            next = min(next2, next3, next5)

            # 2, 3, 5 の倍数の中で最小の ugly number を見つけたので、
            # その値を ugly number のリストに追加する
            ugly.append(next)

            # どの値をリストに追加したのかによって、i2, i3, i5 の値を更新する
            if next == next2:
                i2 += 1
            if next == next3:
                i3 += 1
            if next == next5:
                i5 += 1

        return ugly[-1]

=======
Suggestion 10

def nthUglyNumber(self, n: int) -> int:
        # dp[i] は i 番目の ugly number を表す
        dp = [0] * n
        dp[0] = 1

        # それぞれ 2, 3, 5 を掛けた値を格納するための index
        index2 = 0
        index3 = 0
        index5 = 0

        for i in range(1, n):
            # それぞれの値を掛けたもののうち、最小のものを dp[i] とする
            dp[i] = min(dp[index2] * 2, dp[index3] * 3, dp[index5] * 5)

            # 最小の値を掛けた index をインクリメントする
            if dp[i] == dp[index2] * 2:
                index2 += 1
            if dp[i] == dp[index3] * 3:
                index3 += 1
            if dp[i] == dp[index5] * 5:
                index5 += 1

        return dp[-1]
