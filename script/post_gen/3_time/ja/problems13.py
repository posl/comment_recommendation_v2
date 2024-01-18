Synthesizing 10/10 solutions

=======
Suggestion 1

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 2147483647:
            return 32
        if n % 2 == 0:
            return self.integerReplacement(n/2) + 1
        else:
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1

=======
Suggestion 2

def integerReplacement(self, n: int) -> int:
        # 1の場合は0回
        if n == 1:
            return 0
        # 偶数の場合は割る
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        # 奇数の場合は足すか引くか
        return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

=======
Suggestion 3

def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                count += 1
            else:
                if n == 3:
                    count += 2
                    break
                else:
                    if (n + 1) % 4 == 0:
                        n += 1
                        count += 1
                    else:
                        n -= 1
                        count += 1
        return count

=======
Suggestion 4

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                if n % 4 == 1 or n == 3:
                    n -= 1
                else:
                    n += 1
            count += 1
        return count

=======
Suggestion 5

def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0:
        #    return 1 + self.integerReplacement(n // 2)
        #else:
        #    return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        #if n == 1:
        #    return 0
        #if n % 2 == 0

=======
Suggestion 6

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n == 3 or (n // 2) % 2 == 0:
                n -= 1
            else:
                n += 1
            count += 1
        return count

=======
Suggestion 7

def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n%2 == 0:
                n = n//2
            else:
                if n == 3:
                    n -= 1
                elif bin(n-1).count("1") < bin(n+1).count("1"):
                    n += 1
                else:
                    n -= 1
            count += 1
        return count

=======
Suggestion 8

class Solution:
    def integerReplacement(self, n: int) -> int:
        #bit演算
        #0b1001011
        #0b100101
        #0b10011
        #0b10100
        #0b1010
        #0b101
        #0b110
        #0b11
        #0b100
        #0b10
        #0b1
        #0b0
        #1になるまでに必要な操作の最小回数を出力せよ。
        #nが偶数の場合、nをn÷2に置き換える。
        #nが奇数の場合、n を n + 1 または n - 1 に置き換える。
        #nが1になるまでに必要な操作の最小回数を出力せよ。
        #nが偶数の場合、nをn÷2に置き換える。
        #nが奇数の場合、n を n + 1 または n - 1 に置き換える。
        #nが1になるまでに必要な操作の最小回数を出力せよ。
        #nが偶数の場合、nをn÷2に置き換える。
        #nが奇数の場合、n を n + 1 または n - 1 に置き換える。
        #nが1になるまでに必要な操作の最小回数を出力せよ。
        #nが偶数の場合、nをn÷2に置き換える。
        #nが奇数の場合、n を n + 1 または n - 1 に置き換える。
        #nが1になるまでに必要な操作の最小回数を出力せよ。
        #nが偶数の場合、nをn÷2に置き換える。
        #nが奇数の場合、n を n + 1 または n - 1 に置き

=======
Suggestion 9

def integerReplacement(self, n: int) -> int:
        # 0が含まれる場合
        if n == 0:
            return 32
        # 1が含まれる場合
        if n == 1:
            return 0
        # 2が含まれる場合
        if n == 2:
            return 1
        # 3が含まれる場合
        if n == 3:
            return 2
        # 4が含まれる場合
        if n == 4:
            return 2
        # 5が含まれる場合
        if n == 5:
            return 3
        # 6が含まれる場合
        if n == 6:
            return 3
        # 7が含まれる場合
        if n == 7:
            return 4
        # 8が含まれる場合
        if n == 8:
            return 3
        # 9が含まれる場合
        if n == 9:
            return 4
        # 10が含まれる場合
        if n == 10:
            return 4
        # 11が含まれる場合
        if n == 11:
            return 5
        # 12が含まれる場合
        if n == 12:
            return 4
        # 13が含まれる場合
        if n == 13:
            return 5
        # 14が含まれる場合
        if n == 14:
            return 5
        # 15が含まれる場合
        if n == 15:
            return 6
        # 16が含まれる場合
        if n == 16:
            return 4
        # 17が含まれる場合
        if n == 17:
            return 5
        # 18が含まれる場合
        if n == 18:
            return 5
        # 19が含まれる場合
        if n == 19:
            return 6
        # 20が含まれる場合
        if n == 20:

=======
Suggestion 10

def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                if (n + 1) % 4 == 0 and n != 3:
                    n += 1
                else:
                    n -= 1
            cnt += 1
        return cnt
