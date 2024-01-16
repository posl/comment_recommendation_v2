Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        res = 0
        n = str(n)
        for i in range(len(n)):
            if i == 0:
                if int(n[i]) > 1:
                    res += 10 ** (len(n) - 1)
                elif int(n[i]) == 1:
                    res += int(n[i + 1:]) + 1
            elif i == len(n) - 1:
                if int(n[i]) >= 1:
                    res += 1
            else:
                if int(n[i]) > 1:
                    res += (int(n[:i]) + 1) * 10 ** (len(n) - i - 1)
                elif int(n[i]) == 1:
                    res += int(n[:i]) * 10 ** (len(n) - i - 1) + int(n[i + 1:]) + 1
        return res

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        str_n = str(n)
        length = len(str_n)
        first = int(str_n[0])
        if first == 1:
            return self.countDigitOne(n - int('1' * (length - 1))) + self.countDigitOne(int('1' * (length - 1))) + n - int('1' * (length - 1)) + 1
        else:
            return self.countDigitOne(n - int(str(first) * (length - 1))) + first * self.countDigitOne(int('1' * (length - 1))) + int('1' * (length - 1))

=======
Suggestion 3

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == "1":
                    count += 1
        return count
        # Runtime: 84 ms
        # Memory Usage: 13.9 MB
        # Your runtime beats 5.01 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join([str(i) for i in range(1, n+1)]).count('1')
        # Runtime: 72 ms
        # Memory Usage: 13.8 MB
        # Your runtime beats 6.86 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join([str(i) for i in range(1, n+1)]).count('1')
        # Runtime: 68 ms
        # Memory Usage: 13.8 MB
        # Your runtime beats 7.94 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join(map(str, range(1, n+1))).count('1')
        # Runtime: 64 ms
        # Memory Usage: 13.8 MB
        # Your runtime beats 9.49 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join(map(str, range(1, n+1))).count('1')
        # Runtime: 60 ms
        # Memory Usage: 13.8 MB
        # Your runtime beats 10.80 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join(map(str, range(1, n+1))).count('1')
        # Runtime: 56 ms
        # Memory Usage: 13.8 MB
        # Your runtime beats 13.61 % of python3 submissions.
        # Your memory usage beats 99.97 % of python3 submissions.
        #return ''.join(map(str, range(1, n+1))).count('1')
        # Runtime: 52 ms
        # Memory Usage: 13

=======
Suggestion 4

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        if n < 20:
            return 2
        if n < 100:
            return 20 + self.countDigitOne(n%10)
        if n < 200:
            return 30 + self.countDigitOne(n%100)
        if n < 1000:
            return 300 + self.countDigitOne(n%100)
        if n < 2000:
            return 400 + self.countDigitOne(n%1000)
        if n < 10000:
            return 4000 + self.countDigitOne(n%1000)
        if n < 20000:
            return 5000 + self.countDigitOne(n%10000)
        if n < 100000:
            return 50000 + self.countDigitOne(n%10000)
        if n < 200000:
            return 60000 + self.countDigitOne(n%100000)
        if n < 1000000:
            return 600000 + self.countDigitOne(n%100000)
        if n < 2000000:
            return 700000 + self.countDigitOne(n%1000000)
        if n < 10000000:
            return 7000000 + self.countDigitOne(n%1000000)
        if n < 20000000:
            return 80000000 + self.countDigitOne(n%10000000)
        if n < 100000000:
            return 800000000 + self.countDigitOne(n%10000000)
        if n < 200000000:
            return 900000000 + self.countDigitOne(n%100000000)
        if n < 1000000000:
            return 9000000000 + self.countDigitOne(n%100000000)
        if n < 2000000000:
            return 10000000000 + self.countDigitOne(n%1000000000)
        if n < 10000000000:
            return 100000000000 + self.countDigitOne(n%1000000000)
        if n < 20000000000:
            return 110000000000 + self.countDigitOne(n%10000000000)
        if n < 100000000000:
            return 1100000000000 + self

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count

=======
Suggestion 7

def countDigitOne(self, n: int) -> int:
        ones = 0
        m = 1
        while m <= n:
            a = n//m
            b = n%m
            ones += (a+8)//10*m + (a%10 == 1)*(b+1)
            m *= 10
        return ones

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        if n<0:
            return 0
        if n<10:
            return 1
        count=0
        for i in range(1,n+1):
            count+=str(i).count('1')
        return count
        #return sum([str(i).count('1') for i in range(1,n+1)])

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        else:
            s = str(n)
            l = len(s)
            if s[0] == "1":
                return n - 10**(l-1) + 1 + self.countDigitOne(10**(l-2)-1) + self.countDigitOne(int(s[1:]))
            else:
                return 10**(l-1) + self.countDigitOne(10**(l-2)-1) * (int(s[0])-1) + self.countDigitOne(int(s[1:]))
