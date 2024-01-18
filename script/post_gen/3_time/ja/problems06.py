Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n

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
        if n == 1:
            return 1
        i = 2
        ugly = [1]
        while len(ugly) < n:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                if i % 2 == 0:
                    if i // 2 in ugly:
                        ugly.append(i)
                elif i % 3 == 0:
                    if i // 3 in ugly:
                        ugly.append(i)
                elif i % 5 == 0:
                    if i // 5 in ugly:
                        ugly.append(i)
            i += 1
        return ugly[-1]

=======
Suggestion 4

def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
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
Suggestion 5

def nthUglyNumber(self, n: int) -> int:
        # 1を追加しておく
        ugly = [1]
        # それぞれの倍数を管理するためのポインタ
        i2, i3, i5 = 0, 0, 0
        # n-1個の ugly number を求める
        while len(ugly) < n:
            # それぞれの倍数のうち、最小のものを求める
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            # 求めた ugly number をリストに追加する
            ugly.append(next_ugly)
            # どの倍数を次に使うかを更新する
            if next_ugly == ugly[i2] * 2:
                i2 += 1
            if next_ugly == ugly[i3] * 3:
                i3 += 1
            if next_ugly == ugly[i5] * 5:
                i5 += 1
        # n番目の ugly number を返す
        return ugly[-1]

=======
Suggestion 6

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
Suggestion 7

def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            ugly_numbers.append(min(ugly_numbers[p2] * 2, ugly_numbers[p3] * 3, ugly_numbers[p5] * 5))
            if ugly_numbers[i] == ugly_numbers[p2] * 2:
                p2 += 1
            if ugly_numbers[i] == ugly_numbers[p3] * 3:
                p3 += 1
            if ugly_numbers[i] == ugly_numbers[p5] * 5:
                p5 += 1
        return ugly_numbers[-1]
