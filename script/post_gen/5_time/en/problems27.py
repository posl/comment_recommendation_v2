Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1
        res = 0
        s = str(n)
        length = len(s)
        for i in range(length):
            res += self.helper(s, i, n)
        return res

=======
Suggestion 2

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

=======
Suggestion 3

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1 10 11 12 13 14 15 16 17 18 19 21 31 41 51 61 71 81 91 101
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 13 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12 13 14 14 14 14 14 14 15
        # 1 2  4  4  5  6  7  8  9  10 11 12
        # 1 2  4  4

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
            return 20 + (n % 10) + 10 * self.countDigitOne(n // 10)
        if n < 200:
            return 20 + (n % 10) + 10 * self.countDigitOne(n // 10 - 10)
        if n < 1000:
            return 300 + (n % 100) + 100 * self.countDigitOne(n // 100)
        if n < 2000:
            return 300 + (n % 100) + 100 * self.countDigitOne(n // 100 - 10)
        if n < 10000:
            return 4000 + (n % 1000) + 1000 * self.countDigitOne(n // 1000)
        if n < 20000:
            return 4000 + (n % 1000) + 1000 * self.countDigitOne(n // 1000 - 10)
        if n < 100000:
            return 50000 + (n % 10000) + 10000 * self.countDigitOne(n // 10000)
        if n < 200000:
            return 50000 + (n % 10000) + 10000 * self.countDigitOne(n // 10000 - 10)
        if n < 1000000:
            return 600000 + (n % 100000) + 100000 * self.countDigitOne(n // 100000)
        if n < 2000000:
            return 600000 + (n % 100000) + 100000 * self.countDigitOne(n // 100000 - 10)
        if n < 10000000:
            return 7000000 + (n % 1000000) + 1000000 * self.countDigitOne(n // 1000000)
        if n < 20000000:
            return 7000000 + (n % 1000000) + 1000000 * self.countDigitOne(n // 1000000 - 10)
        if n < 100000000:
            return 80000000 + (n %

=======
Suggestion 5

def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        if n < 10: return 1
        if n < 20: return 2
        if n < 100: return 20 + self.countDigitOne(n % 10) + (n // 10 - 2) * 10
        if n < 200: return 21 + self.countDigitOne(n % 100) + (n // 100 - 2) * 100
        if n < 1000: return 300 + self.countDigitOne(n % 100) + (n // 100 - 3) * 100
        if n < 2000: return 301 + self.countDigitOne(n % 1000) + (n // 1000 - 3) * 1000
        if n < 10000: return 4000 + self.countDigitOne(n % 1000) + (n // 1000 - 4) * 1000
        if n < 20000: return 4001 + self.countDigitOne(n % 10000) + (n // 10000 - 4) * 10000
        if n < 100000: return 50000 + self.countDigitOne(n % 10000) + (n // 10000 - 5) * 10000
        if n < 200000: return 50001 + self.countDigitOne(n % 100000) + (n // 100000 - 5) * 100000
        if n < 1000000: return 600000 + self.countDigitOne(n % 100000) + (n // 100000 - 6) * 100000
        if n < 2000000: return 600001 + self.countDigitOne(n % 1000000) + (n // 1000000 - 6) * 1000000
        if n < 10000000: return 7000000 + self.countDigitOne(n % 1000000) + (n // 1000000 - 7) * 1000000
        if n < 20000000: return 7000001 + self.countDigitOne(n % 10000000) + (n // 10000000 - 7) * 100000

=======
Suggestion 6

def countDigitOne(self, n: int) -> int:
        ones, m = 0, 1
        while m <= n:
            a, b = n // m, n % m
            ones += (a + 8) // 10 * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return ones

=======
Suggestion 7

class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1 <= n <= 2^31 - 1
        # 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        # 21, 31, 41, 51, 61, 71, 81, 91,
        # 101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
        # 201, 211, 221, 231, 241, 251, 261, 271, 281, 291,
        # 301, 311, 321, 331, 341, 351, 361, 371, 381, 391,
        # 401, 411, 421, 431, 441, 451, 461, 471, 481, 491,
        # 501, 511, 521, 531, 541, 551, 561, 571, 581, 591,
        # 601, 611, 621, 631, 641, 651, 661, 671, 681, 691,
        # 701, 711, 721, 731, 741, 751, 761, 771, 781, 791,
        # 801, 811, 821, 831, 841, 851, 861, 871, 881, 891,
        # 901, 911, 921, 931, 941, 951, 961, 971, 981, 991,
        # 1001, 1011, 1021, 1031, 1041, 1051, 1061, 1071, 1081, 1091,
        # 1101, 1111, 1121, 1131, 1141, 1151, 1161, 1171, 1181, 1191,
        # 1201, 1211, 1221, 1231, 1241, 1251, 1261, 1271, 1281, 1291,
        # 1301, 1311

=======
Suggestion 8

def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        if n < 10: return 1
        if n < 20: return 11
        s = str(n)
        m = len(s)
        if int(s[0]) == 1:
            return (n - 10**(m-1) + 1) + self.countDigitOne(10**(m-1)-1) + self.countDigitOne(n - 10**(m-1))
        else:
            return 10**(m-1) + int(s[0]) * self.countDigitOne(10**(m-1)-1) + self.countDigitOne(n - int(s[0])*10**(m-1))

=======
Suggestion 9

def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        s = str(n)
        l = len(s)
        # 1. count the number of 1 in the first digit
        # 2. count the number of 1 in the other digits
        # 3. count the number of 1 in the first digit of the next number
        # 4. count the number of 1 in the other digits of the next number
        # 5. count the number of 1 in the first digit of the next number
        # 6. count the number of 1 in the other digits of the next number
        # 7. count the number of 1 in the first digit of the next number
        # 8. count the number of 1 in the other digits of the next number
        # 9. count the number of 1 in the first digit of the next number
        # 10. count the number of 1 in the other digits of the next number
        # 11. count the number of 1 in the first digit of the next number
        # 12. count the number of 1 in the other digits of the next number
        # 13. count the number of 1 in the first digit of the next number
        # 14. count the number of 1 in the other digits of the next number
        # 15. count the number of 1 in the first digit of the next number
        # 16. count the number of 1 in the other digits of the next number
        # 17. count the number of 1 in the first digit of the next number
        # 18. count the number of 1 in the other digits of the next number
        # 19. count the number of 1 in the first digit of the next number
        # 20. count the number of 1 in the other digits of the next number
        # 21. count the number of 1 in the first digit of the next number
        # 22. count the number of 1 in the other digits of the next number
        # 23. count the number of 1 in the first digit of the next number
        # 24. count the number of 1

=======
Suggestion 10

def countDigitOne(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            count += str(i).count("1")
        return count
