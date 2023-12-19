Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(101))
print(countDigitOne(1001))
print(countDigitOne(10001))
print(countDigitOne(100001))
print(countDigitOne(1000001))
print(countDigitOne(10000001))
print(countDigitOne(100000001))
print(countDigitOne(1000000001))
print(countDigitOne(10000000001))
print(countDigitOne(100000000001))
print(countDigitOne(1000000000001))
print(countDigitOne(10000000000001))
print(countDigitOne(100000000000001))
print(countDigitOne(1000000000000001))
print(countDigitOne(10000000000000001))
print(countDigitOne(100000000000000001))
print(countDigitOne(1000000000000000001))
print(countDigitOne(10000000000000000001))
print(countDigitOne(100000000000000000001))
print(countDigitOne(1000000000000000000001))
print(countDigitOne(10000000000000000000001))
print(countDigitOne(100000000000000000000001))
print(countDigitOne(1000000000000000000000001))
print(countDigitOne(10000000000000000000000001))
print(countDigitOne(100000000000000000000000001))
print(countDigitOne(1000000000000000000000000001))
print(countDigitOne(10000000000000000000000000001))
print(countDigitOne(100000000000000000000000000001))
print(countDigitOne(1000000000000000000000000000001))
print(countDigitOne(10000000000000000000000000000001))
print(countDigitOne(100000000000000000000000000000001))
print(countDigi

=======
Suggestion 2

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    if n < 10:
        return 1
    if n < 20:
        return 2
    if n < 100:
        return n//10 + 10 + countDigitOne(n%10)
    if n < 200:
        return n//100 + 20 + countDigitOne(n%100)
    if n < 1000:
        return n//100 + 10*countDigitOne(n%100)
    if n < 2000:
        return n//1000 + 100 + countDigitOne(n%1000)
    if n < 10000:
        return n//1000 + 10*countDigitOne(n%1000)
    if n < 20000:
        return n//10000 + 1000 + countDigitOne(n%10000)
    if n < 100000:
        return n//10000 + 10*countDigitOne(n%10000)
    if n < 200000:
        return n//100000 + 10000 + countDigitOne(n%100000)
    if n < 1000000:
        return n//100000 + 10*countDigitOne(n%100000)
    if n < 2000000:
        return n//1000000 + 100000 + countDigitOne(n%1000000)
    if n < 10000000:
        return n//1000000 + 10*countDigitOne(n%1000000)
    if n < 20000000:
        return n//10000000 + 1000000 + countDigitOne(n%10000000)
    if n < 100000000:
        return n//10000000 + 10*countDigitOne(n%10000000)
    if n < 200000000:
        return n//100000000 + 10000000 + countDigitOne(n%100000000)
    if n < 1000000000:
        return n//100000000 + 10*countDigitOne(n%100000000)
    if n < 2000000000:
        return n//1000000000 + 100000000 + countDigitOne(n%1000000000

=======
Suggestion 3

def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

n = 13
print(countDigitOne(n))

n = 0
print(countDigitOne(n))

=======
Suggestion 4

def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(100))

=======
Suggestion 5

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    count = 0
    for i in range(1, n+1):
        while i > 0:
            if i % 10 == 1:
                count += 1
            i //= 10
    return count

=======
Suggestion 6

def main():
    n = 13
    print(countDigitOne(n))

=======
Suggestion 7

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(20))
print(countDigitOne(21))
print(countDigitOne(22))
print(countDigitOne(30))
print(countDigitOne(31))
print(countDigitOne(32))
print(countDigitOne(100))
print(countDigitOne(101))
print(countDigitOne(102))
print(countDigitOne(110))
print(countDigitOne(111))
print(countDigitOne(112))
print(countDigitOne(120))
print(countDigitOne(121))
print(countDigitOne(122))
print(countDigitOne(200))
print(countDigitOne(201))
print(countDigitOne(202))
print(countDigitOne(210))
print(countDigitOne(211))
print(countDigitOne(212))
print(countDigitOne(220))
print(countDigitOne(221))
print(countDigitOne(222))
print(countDigitOne(1000))
print(countDigitOne(1001))
print(countDigitOne(1002))
print(countDigitOne(1010))
print(countDigitOne(1011))
print(countDigitOne(1012))
print(countDigitOne(1020))
print(countDigitOne(1021))
print(countDigitOne(1022))
print(countDigitOne(1100))
print(countDigitOne(1101))
print(countDigitOne(1102))
print(countDigitOne(1110))
print(countDigitOne(1111))
print(countDigitOne(1112))
print(countDigitOne(1120))
print(countDigitOne(1121))
print(countDigitOne(1122))
print(countDigitOne(1200))
print(countDigitOne(1201))
print(countDigitOne(1202))
print(countDigitOne(1210))
print(countDigitOne(1211))
print(countDigitOne(1212))
print(countDigitOne(1220))
print(countDigitOne(

=======
Suggestion 8

def countDigitOne(n):
    count = 0
    for i in range(1, n + 1):
        for j in str(i):
            if j == '1':
                count += 1
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(14))
print(countDigitOne(15))
print(countDigitOne(16))
print(countDigitOne(17))
print(countDigitOne(18))
print(countDigitOne(19))
print(countDigitOne(20))
print(countDigitOne(21))
print(countDigitOne(22))
print(countDigitOne(23))
print(countDigitOne(24))
print(countDigitOne(25))
print(countDigitOne(26))
print(countDigitOne(27))
print(countDigitOne(28))
print(countDigitOne(29))
print(countDigitOne(30))
print(countDigitOne(31))
print(countDigitOne(32))
print(countDigitOne(33))
print(countDigitOne(34))
print(countDigitOne(35))
print(countDigitOne(36))
print(countDigitOne(37))
print(countDigitOne(38))
print(countDigitOne(39))
print(countDigitOne(40))
print(countDigitOne(41))
print(countDigitOne(42))
print(countDigitOne(43))
print(countDigitOne(44))
print(countDigitOne(45))
print(countDigitOne(46))
print(countDigitOne(47))
print(countDigitOne(48))
print(countDigitOne(49))
print(countDigitOne(50))
print(countDigitOne(51))
print(countDigitOne(52))
print(countDigitOne(53))
print(countDigitOne(54))
print(countDigitOne(55))
print(countDigitOne(56))
print(countDigitOne(57))
print(countDigitOne(58))
print(countDigitOne(59))
print(countDigitOne(60))
print(countDigitOne(61))
print(countDigitOne(62))
print(countDigitOne(63))
print(countDigitOne(64))
print(countDigitOne(65))
print(countDigitOne(66))
print(countDigitOne(67))
print(countDigitOne(68))
print(countDigitOne(69))
print(countDigitOne(70))
print(countDigitOne(71))
print(countDigitOne

=======
Suggestion 9

def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        for j in str(i):
            if j == '1':
                count += 1
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))

=======
Suggestion 10

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    ones, m = 0, 1
    while m <= n:
        ones += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n % m + 1)
        m *= 10
    return ones

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(10))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))
# Solution:
# 1. 从最低位开始，每次判断该位数字是否为1，若是则计数加1
# 2. 然后判断该位数字是否为0，若是则计数加上高位数字+1
# 3. 然后判断该位数字是否大于1，若是则计数加上m（m为当前位的位数）
# 4. 然后将m乘以10，继续判断下一位数字
# 5. 直到m大于n
# 6. 返回计数
# Beats: 90.34%
# Runtime: 20ms
# hard
