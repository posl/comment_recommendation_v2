Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        res = 0
        for i in range(1, len(str(n))+1):
            res += self.count(n, i)
        return res

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        # 1. get the number of digits
        digits = 0
        temp = n
        while temp > 0:
            digits += 1
            temp = temp // 10
        # 2. get the number of 1s for each digit
        count = 0
        for i in range(digits):
            # 2.1 get the number of 1s for each digit
            # 2.1.1 get the number of 1s for the digit 1
            if i == 0:
                count += (n // 10 ** (i + 1)) * (10 ** i)
                if n % 10 ** (i + 1) >= 1:
                    count += n % 10 ** i + 1
            # 2.1.2 get the number of 1s for the digit 2 to the last digit
            else:
                count += (n // 10 ** (i + 1)) * (10 ** i)
                if n % 10 ** (i + 1) >= 10 ** i:
                    count += 10 ** i
                else:
                    count += n % 10 ** i + 1
        return count

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        # 1. 求出n的位数
        length = len(str(n))
        # 2. 求出n的最高位
        first = int(str(n)[0])
        # 3. 求出n的最高位为1时，其余位数的1的个数
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        # 4. 求出最高位不为1时，其余位数的1的个数
        # 4.1 求出最高位不为1时，其余位数的1的个数
        # 4.2 求出最高位为1时，其余位数的1的个数
        # 4.3 求出最高位为1时，其余位数的1的个数
        high = self.countDigitOne(10 ** (length - 1) - 1)
        low = self.countDigitOne(n - 10 ** (length - 1) * first)
        mid = self.countDigitOne(10 ** (length - 1) - 1)
        if first == 1:
            return low + high + mid + 1
        else:
            return low + high + mid + 10 ** (length - 1)

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        if n < 20:
            return 2
        if n < 100:
            if n % 10 == 0:
                return int(n / 10)
            else:
                return int(n / 10) + 1
        if n < 200:
            return int(n / 100) + self.countDigitOne(n % 100) + 100
        if n < 1000:
            if n % 100 == 0:
                return int(n / 100) + 1
            else:
                return int(n / 100) + self.countDigitOne(n % 100) + 100
        if n < 2000:
            return int(n / 1000) + self.countDigitOne(n % 1000) + 1000
        if n < 10000:
            if n % 1000 == 0:
                return int(n / 1000) + 1
            else:
                return int(n / 1000) + self.countDigitOne(n % 1000) + 1000
        if n < 20000:
            return int(n / 10000) + self.countDigitOne(n % 10000) + 10000
        if n < 100000:
            if n % 10000 == 0:
                return int(n / 10000) + 1
            else:
                return int(n / 10000) + self.countDigitOne(n % 10000) + 10000
        if n < 200000:
            return int(n / 100000) + self.countDigitOne(n % 100000) + 100000
        if n < 1000000:
            if n % 100000 == 0:
                return int(n / 100000) + 1
            else:
                return int(n / 100000) + self.countDigitOne(n % 100000) + 100000
        if n < 2000000:
            return int(n / 1000000) + self.countDigitOne(n % 1000000) + 1000000
        if n < 10000000:
            if n % 1000000 == 0:

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        str_n = str(n)
        first = int(str_n[0])
        last = int(str_n[1:])
        length = len(str_n)
        if first == 1:
            return self.countDigitOne(last) + self.countDigitOne(10 ** (length - 1) - 1) + last + 1
        else:
            return first * self.countDigitOne(10 ** (length - 1) - 1) + self.countDigitOne(last) + 10 ** (length - 1)

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        num = str(n)
        length = len(num)
        first = int(num[0])
        if first == 1:
            return self.countDigitOne(int(num[1:])) + self.countDigitOne(int('9'*(length-1)))
        else:
            return first*self.countDigitOne(int('9'*(length-1))) + self.countDigitOne(int(num[1:])) + 10**(length-1)

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        if n < 20:
            return 1 + self.countDigitOne(n - 10)
        if n < 100:
            return 10 + self.countDigitOne(n - 20)
        if n < 200:
            return 20 + self.countDigitOne(n - 100)
        if n < 1000:
            return 100 + 2 * self.countDigitOne(n - 200)
        if n < 2000:
            return 200 + 2 * self.countDigitOne(n - 1000)
        if n < 10000:
            return 1000 + 3 * self.countDigitOne(n - 2000)
        if n < 20000:
            return 2000 + 3 * self.countDigitOne(n - 10000)
        if n < 100000:
            return 10000 + 4 * self.countDigitOne(n - 20000)
        if n < 200000:
            return 20000 + 4 * self.countDigitOne(n - 100000)
        if n < 1000000:
            return 100000 + 5 * self.countDigitOne(n - 200000)
        if n < 2000000:
            return 200000 + 5 * self.countDigitOne(n - 1000000)
        if n < 10000000:
            return 1000000 + 6 * self.countDigitOne(n - 2000000)
        if n < 20000000:
            return 2000000 + 6 * self.countDigitOne(n - 10000000)
        if n < 100000000:
            return 10000000 + 7 * self.countDigitOne(n - 20000000)
        if n < 200000000:
            return 20000000 + 7 * self.countDigitOne(n - 100000000)
        if n < 1000000000:
            return 100000000 + 8 * self.countDigitOne(n - 200000000)
        if n < 2000000000:
            return 200000000 + 8 * self.countDigitOne(n - 1000000000)
        return 1000000000 + 9 * self.count

=======
Suggestion 10

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        count = 0
        for i in range(1, n+1):
            count += str(i).count('1')
        return count
