Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        if n<=0:
            return 0
        if n<10:
            return 1
        count=0
        for i in range(1,n+1):
            count+=str(i).count('1')
        return count

=======
Suggestion 3

class Solution:
    def countDigitOne(self, n: int) -> int:
        # the idea is to count the number of 1s in each digit
        # for example, 1234
        # 1. count the number of 1s in the thousands digit
        # 2. count the number of 1s in the hundreds digit
        # 3. count the number of 1s in the tens digit
        # 4. count the number of 1s in the ones digit
        # then add them together to get the final result
        # for example, 1234
        # 1. 1 * 1000 = 1000, since there are 1234 numbers that has 1 as the thousands digit
        # 2. 2 * 100 = 200, since there are 200 numbers that has 1 as the hundreds digit
        # 3. 1 * 10 = 10, since there are 10 numbers that has 1 as the tens digit
        # 4. 0 * 1 = 0, since there are 0 numbers that has 1 as the ones digit
        # so the final result is 1000 + 200 + 10 + 0 = 1210
        # for example, 101
        # 1. 0 * 100 = 0, since there are 0 numbers that has 1 as the thousands digit
        # 2. 1 * 10 = 10, since there are 10 numbers that has 1 as the hundreds digit
        # 3. 1 * 1 = 1, since there is 1 number that has 1 as the tens digit
        # 4. 0 * 0 = 0, since there are 0 numbers that has 1 as the ones digit
        # so the final result is 0 + 10 + 1 + 0 = 11
        # for example, 111
        # 1. 1 * 100 = 100, since there are 100 numbers that has 1 as the thousands digit
        # 2. 1 * 10 = 10, since there are 10 numbers that has 1 as the hundreds digit
        # 3. 1 * 1 = 1, since there is 1 number that has 1 as the tens digit

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        if n == 10:
            return 2
        if n < 20:
            return 1 + self.countDigitOne(n-10)
        if n < 100:
            return 10 + self.countDigitOne(n-10)
        if n < 200:
            return 20 + self.countDigitOne(n-100)
        if n < 1000:
            return 100 + self.countDigitOne(n-100)
        if n < 2000:
            return 200 + self.countDigitOne(n-1000)
        if n < 10000:
            return 1000 + self.countDigitOne(n-1000)
        if n < 20000:
            return 2000 + self.countDigitOne(n-10000)
        if n < 100000:
            return 10000 + self.countDigitOne(n-10000)
        if n < 200000:
            return 20000 + self.countDigitOne(n-100000)
        if n < 1000000:
            return 100000 + self.countDigitOne(n-100000)
        if n < 2000000:
            return 200000 + self.countDigitOne(n-1000000)
        if n < 10000000:
            return 1000000 + self.countDigitOne(n-1000000)
        if n < 20000000:
            return 2000000 + self.countDigitOne(n-10000000)
        if n < 100000000:
            return 10000000 + self.countDigitOne(n-10000000)
        if n < 200000000:
            return 20000000 + self.countDigitOne(n-100000000)
        if n < 1000000000:
            return 100000000 + self.countDigitOne(n-100000000)
        if n < 2000000000:
            return 200000000 + self.countDigitOne(n-1000000000)
        if n == 2000000000:
            return 2000000000 + self.countDigitOne(n-1000000000)
        return 0

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        if n == 10:
            return 2
        if n < 20:
            return 11
        if n < 100:
            return 20 + self.countDigitOne(n % 10)
        if n < 200:
            return 20 + self.countDigitOne(n % 100) + n % 100 + 1
        if n < 1000:
            return 300 + self.countDigitOne(n % 100)
        if n < 2000:
            return 300 + self.countDigitOne(n % 1000) + n % 1000 + 1
        if n < 10000:
            return 4000 + self.countDigitOne(n % 1000)
        if n < 20000:
            return 4000 + self.countDigitOne(n % 10000) + n % 10000 + 1
        if n < 100000:
            return 50000 + self.countDigitOne(n % 10000)
        if n < 200000:
            return 50000 + self.countDigitOne(n % 100000) + n % 100000 + 1
        if n < 1000000:
            return 600000 + self.countDigitOne(n % 100000)
        if n < 2000000:
            return 600000 + self.countDigitOne(n % 1000000) + n % 1000000 + 1
        if n < 10000000:
            return 7000000 + self.countDigitOne(n % 1000000)
        if n < 20000000:
            return 7000000 + self.countDigitOne(n % 10000000) + n % 10000000 + 1
        if n < 100000000:
            return 80000000 + self.countDigitOne(n % 10000000)
        if n < 200000000:
            return 80000000 + self.countDigitOne(n % 100000000) + n % 100000000 + 1
        if n < 1000000000:
            return 900000000 + self.countDigitOne(n % 100000000)
        if n < 2000000000

=======
Suggestion 6

    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        elif n < 20:
            return 2
        elif n < 100:
            return 20 + (n % 10 + 1) + self.countDigitOne(n % 10)
        elif n < 200:
            return 20 + 10 * self.countDigitOne(n % 100) + self.countDigitOne(n % 100)
        elif n < 1000:
            return 300 + self.countDigitOne(n % 100)
        elif n < 2000:
            return 300 + 100 * self.countDigitOne(n % 1000) + self.countDigitOne(n % 1000)
        elif n < 10000:
            return 4000 + self.countDigitOne(n % 1000)
        elif n < 20000:
            return 4000 + 1000 * self.countDigitOne(n % 10000) + self.countDigitOne(n % 10000)
        elif n < 100000:
            return 50000 + self.countDigitOne(n % 10000)
        elif n < 200000:
            return 50000 + 10000 * self.countDigitOne(n % 100000) + self.countDigitOne(n % 100000)
        elif n < 1000000:
            return 600000 + self.countDigitOne(n % 100000)
        elif n < 2000000:
            return 600000 + 100000 * self.countDigitOne(n % 1000000) + self.countDigitOne(n % 1000000)
        elif n < 10000000:
            return 7000000 + self.countDigitOne(n % 1000000)
        elif n < 20000000:
            return 7000000 + 1000000 * self.countDigitOne(n % 10000000) + self.countDigitOne(n % 10000000)
        elif n < 100000000:
            return 80000000 + self.countDigitOne(n % 10000000)
        elif n < 200000000:
            return 80000000 + 10000000 * self.countDigitOne(n % 100000000) + self.countDigitOne(n % 100000000)
        elif n <

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        res = 0
        i = 1
        while i <= n:
            divider = i * 10
            res += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return res

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            count += str(i).count('1')
        return count

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        count, factor = 0, 1
        while n//factor != 0:
            lower, curr, higher = n - (n//factor) * factor, (n//factor) % 10, n//(factor*10)
            if curr == 0:
                count += higher * factor
            elif curr == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
            factor *= 10
        return count

=======
Suggestion 10

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        num = n
        digits = 0
        while num > 0:
            num = num // 10
            digits += 1
        num = n
        first = num // (10 ** (digits - 1))
        rest = num % (10 ** (digits - 1))
        if first == 1:
            return self.countDigitOne(rest) + self.countDigitOne(10 ** (digits - 1) - 1) + rest + 1
        else:
            return self.countDigitOne(rest) + self.countDigitOne(10 ** (digits - 1) - 1) + (first) * (digits - 1) * (10 ** (digits - 2))
