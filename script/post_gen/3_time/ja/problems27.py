Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        # 1桁目の1の個数
        ans = 0
        # 10の桁数
        keta = 1
        # 1の桁数
        ones = 1
        while n >= keta:
            # 1の桁数 * 10の桁数
            ans += ones * (n // (keta * 10))
            # 1の桁数 * min(10の桁数, n % (10の桁数) + 1)
            ans += min(ones, n % (keta * 10) + 1)
            # 1の桁数を1つ増やす
            ones *= 10
            # 10の桁数を1つ増やす
            keta *= 10
        return ans

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        elif n < 10:
            return 1
        else:
            s = str(n)
            l = len(s)
            # 1の位が1の場合
            if int(s[-1]) == 1:
                return self.countDigitOne(n-1) + self.countDigitOne(n-2**(l-1)) + n - 2**(l-1) + 1
            else:
                return self.countDigitOne(n-1) + self.countDigitOne(n-1) * 10**(l-1) + 10**(l-1)

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        pass

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        # 1桁目の1の数
        first = int(str(n)[0])
        # 1桁目以外の1の数
        other = int(str(n)[1:])
        # 1桁目が1の場合
        if first == 1:
            return self.countDigitOne(10 ** (len(str(n)) - 1) - 1) + self.countDigitOne(other) + other + 1
        # 1桁目が1以外の場合
        else:
            return first * self.countDigitOne(10 ** (len(str(n)) - 1) - 1) + self.countDigitOne(other) + 10 ** (len(str(n)) - 1)

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            ans += str(i).count('1')
        return ans

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        def count_digit_one(n):
            if n < 1:
                return 0
            q, x, ans = n, 1, 0
            while q > 0:
                digit = q % 10
                q //= 10
                ans += q * x
                if digit == 1:
                    ans += n % x + 1
                elif digit > 1:
                    ans += x
                x *= 10
            return ans
        return count_digit_one(n)

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        s = str(n)
        l = len(s)
        r = 0
        if s[0] == '1':
            r += int(s[1:]) + 1
        else:
            r += 10 ** (l - 1)
        r += int(s[0]) * (l - 1) * (10 ** (l - 2))
        return r + self.countDigitOne(int(s[1:]))

=======
Suggestion 8

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1桁目、2桁目、3桁目...と順に見ていく
        # 例えば、n=12345のとき、
        # 1桁目の1は、1,11,21,31,41,51,61,71,81,91,101,111,121,131,141,151,161,...,12341,12351の、
        # 1,11,21,31,41,51,61,71,81,91,101,111,121,131,141,151,161,...,12341,12351の11個に含まれる
        # 2桁目の1は、10,11,12,13,14,15,16,17,18,19,110,111,112,113,114,115,116,117,118,119,120,121,...,12319,12320の、
        # 10,11,12,13,14,15,16,17,18,19,110,111,112,113,114,115,116,117,118,119,120,121,...,12319,12320の21個に含まれる
        # 3桁目の1は、100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,...,12309,12310の、
        # 100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,...,12309,12310の112個に含まれる
        # 4桁目の1は、1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,...,12209,12210の、
        # 1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,...,12209,12210の1000個に含まれる
        # 5桁目
