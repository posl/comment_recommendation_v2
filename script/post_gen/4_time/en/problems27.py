Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        if n == 0: return 0
        if n < 10: return 1
        if n < 20: return 2
        if n < 100: return 20 + 1 * (n - 10)
        if n < 200: return 20 + self.countDigitOne(n - 100) + 100
        if n < 1000: return 300 + 2 * self.countDigitOne(n - 200)
        if n < 2000: return 300 + self.countDigitOne(n - 1000) + 1000
        if n < 10000: return 4000 + 3 * self.countDigitOne(n - 2000)
        if n < 20000: return 4000 + self.countDigitOne(n - 10000) + 10000
        if n < 100000: return 50000 + 4 * self.countDigitOne(n - 20000)
        if n < 200000: return 50000 + self.countDigitOne(n - 100000) + 100000
        if n < 1000000: return 600000 + 5 * self.countDigitOne(n - 200000)
        if n < 2000000: return 600000 + self.countDigitOne(n - 1000000) + 1000000
        if n < 10000000: return 7000000 + 6 * self.countDigitOne(n - 2000000)
        if n < 20000000: return 7000000 + self.countDigitOne(n - 10000000) + 10000000
        if n < 100000000: return 80000000 + 7 * self.countDigitOne(n - 20000000)
        if n < 200000000: return 80000000 + self.countDigitOne(n - 100000000) + 100000000
        if n < 1000000000: return 900000000 + 8 * self.countDigitOne(n - 200000000)
        if n < 2000000000: return 900000000 + self.countDigitOne(n - 1000000000) + 1000000000
        return 0

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        if n<10:
            return 1
        strn = str(n)
        first = int(strn[0])
        length = len(strn)
        if first==1:
            return self.countDigitOne(int(strn[1:]))+self.countDigitOne(int(strn[1:]))+int(strn[1:])+1
        else:
            return self.countDigitOne(int(strn[1:]))+first*self.countDigitOne(10**(length-1))+10**(length-1)

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        # 1. 1~9
        # 2. 10~99
        # 3. 100~999
        # 4. 1000~9999
        # 5. 10000~99999
        # 6. 100000~999999
        # 7. 1000000~9999999
        # 8. 10000000~99999999
        # 9. 100000000~999999999
        # 10. 1000000000~2147483647
        # 1~9: 1
        # 10~99: 10 + 9*1
        # 100~999: 100 + 9*20
        # 1000~9999: 1000 + 9*300
        # 10000~99999: 10000 + 9*4000
        # 100000~999999: 100000 + 9*50000
        # 1000000~9999999: 1000000 + 9*600000
        # 10000000~99999999: 10000000 + 9*7000000
        # 100000000~999999999: 100000000 + 9*80000000
        # 1000000000~2147483647: 1000000000 + 9*900000000
        if n < 1:
            return 0
        if n < 10:
            return 1
        if n < 100:
            return 20
        if n < 1000:
            return 300
        if n < 10000:
            return 4000
        if n < 100000:
            return 50000
        if n < 1000000:
            return 600000
        if n < 10000000:
            return 7000000
        if n < 100000000:
            return 80000000
        if n < 1000000000:
            return 900000000
        if n < 2147483647:
            return 1000000000
        return 0

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 9:
            return 1
        elif n <= 99:
            return 20
        elif n <= 999:
            return 300
        elif n <= 9999:
            return 4000
        elif n <= 99999:
            return 50000
        elif n <= 999999:
            return 600000
        elif n <= 9999999:
            return 7000000
        elif n <= 99999999:
            return 80000000
        elif n <= 999999999:
            return 900000000
        else:
            return 0

=======
Suggestion 5

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1 ~ 9: 1
        # 10 ~ 99: 20
        # 100 ~ 999: 300
        # 1000 ~ 9999: 4000
        # 10000 ~ 99999: 50000
        # ...
        # 1000000000 ~ 9999999999: 10000000000
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        
        # 1 ~ 9: 1
        # 10 ~ 99: 20
        # 100 ~ 999: 300
        # 1000 ~ 9999: 4000
        # 10000 ~ 99999: 50000
        # ...
        # 1000000000 ~ 9999999999: 10000000000
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~ 10^(i+1)-1: (i+1) * 10^i
        # 10^i ~

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        if n < 20:
            return 2
        if n < 100:
            return 20 + self.countDigitOne(n%10) + self.countDigitOne(n//10)
        if n < 200:
            return 30 + self.countDigitOne(n%100) + self.countDigitOne(n//100)
        if n < 1000:
            return 300 + self.countDigitOne(n%100) + self.countDigitOne(n//100)
        if n < 2000:
            return 400 + self.countDigitOne(n%1000) + self.countDigitOne(n//1000)
        if n < 10000:
            return 4000 + self.countDigitOne(n%1000) + self.countDigitOne(n//1000)
        if n < 20000:
            return 5000 + self.countDigitOne(n%10000) + self.countDigitOne(n//10000)
        if n < 100000:
            return 50000 + self.countDigitOne(n%10000) + self.countDigitOne(n//10000)
        if n < 200000:
            return 60000 + self.countDigitOne(n%100000) + self.countDigitOne(n//100000)
        if n < 1000000:
            return 600000 + self.countDigitOne(n%100000) + self.countDigitOne(n//100000)
        if n < 2000000:
            return 700000 + self.countDigitOne(n%1000000) + self.countDigitOne(n//1000000)
        if n < 10000000:
            return 7000000 + self.countDigitOne(n%1000000) + self.countDigitOne(n//1000000)
        if n < 20000000:
            return 8000000 + self.countDigitOne(n%10000000) + self.countDigitOne(n//10000000)
        if n < 100000000:
            return 80000000 + self.countDigitOne(n%10000000) + self.countDigitOne(n//10000000)
        if n < 200000000:
            return 90000000 + self.countDigitOne(n%100000000) + self.countDigit

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        n_str = str(n)
        n_len = len(n_str)
        first_digit = int(n_str[0])
        other_digits = int(n_str[1:])
        if first_digit == 1:
            return self.countDigitOne(other_digits) + self.countDigitOne(10**(n_len-1)-1) + other_digits + 1
        else:
            return first_digit*self.countDigitOne(10**(n_len-1)-1) + 10**(n_len-1) + self.countDigitOne(other_digits)

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        res = 0
        i = 1
        while i <= n:
            divider = i * 10
            res += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return res

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        if n < 100:
            return 10 + self.countDigitOne(n - 10)
        if n < 1000:
            return 100 + 2 * self.countDigitOne(n - 100)
        if n < 10000:
            return 1000 + 3 * self.countDigitOne(n - 1000)
        if n < 100000:
            return 10000 + 4 * self.countDigitOne(n - 10000)
        if n < 1000000:
            return 100000 + 5 * self.countDigitOne(n - 100000)
        if n < 10000000:
            return 1000000 + 6 * self.countDigitOne(n - 1000000)
        if n < 100000000:
            return 10000000 + 7 * self.countDigitOne(n - 10000000)
        if n < 1000000000:
            return 100000000 + 8 * self.countDigitOne(n - 100000000)
        return 1000000000 + 9 * self.countDigitOne(n - 1000000000)
