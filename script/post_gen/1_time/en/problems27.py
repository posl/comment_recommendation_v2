Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count

=======
Suggestion 2

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    ones = 0
    m = 1
    while m <= n:
        a = n // m
        b = n % m
        ones += (a + 8) // 10 * m + (a % 10 == 1) * (b + 1)
        m *= 10
    return ones

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(14))
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
print(countDigitOne(70

=======
Suggestion 3

def countDigitOne(n):
    res = 0
    for i in range(1, n+1):
        res += str(i).count('1')
    return res

=======
Suggestion 4

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n<=0:
        return 0
    if n<10:
        return 1
    if n<100:
        return 20
    if n<1000:
        return 300
    if n<10000:
        return 4000
    if n<100000:
        return 50000
    if n<1000000:
        return 600000
    if n<10000000:
        return 7000000
    if n<100000000:
        return 80000000
    if n<1000000000:
        return 900000000
    if n==1000000000:
        return 1000000000
    return 0

=======
Suggestion 5

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n+1):
        for j in str(i):
            if j == '1':
                count += 1
    return count

=======
Suggestion 6

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
        return 20 + countDigitOne(n % 10) + countDigitOne(n / 10 - 1)
    if n < 200:
        return 20 + countDigitOne(n % 100) + countDigitOne(n / 100)
    if n < 1000:
        return 300 + countDigitOne(n % 100) + countDigitOne(n / 100 - 1)
    if n < 2000:
        return 300 + countDigitOne(n % 1000) + countDigitOne(n / 1000)
    if n < 10000:
        return 4000 + countDigitOne(n % 1000) + countDigitOne(n / 1000 - 1)
    if n < 20000:
        return 4000 + countDigitOne(n % 10000) + countDigitOne(n / 10000)
    if n < 100000:
        return 50000 + countDigitOne(n % 10000) + countDigitOne(n / 10000 - 1)
    if n < 200000:
        return 50000 + countDigitOne(n % 100000) + countDigitOne(n / 100000)
    if n < 1000000:
        return 600000 + countDigitOne(n % 100000) + countDigitOne(n / 100000 - 1)
    if n < 2000000:
        return 600000 + countDigitOne(n % 1000000) + countDigitOne(n / 1000000)
    if n < 10000000:
        return 7000000 + countDigitOne(n % 1000000) + countDigitOne(n / 1000000 - 1)
    if n < 20000000:
        return 7000000 + countDigitOne(n % 10000000) + countDigitOne(n / 10000000)
    if n < 100000000:
        return 80000000 + countDigitOne(n % 10000000) + count

=======
Suggestion 7

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    elif n < 10:
        return 1
    else:
        return countDigitOne(n//10) + countDigitOne(n%10)

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

=======
Suggestion 8

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    elif n < 10:
        return 1
    elif n < 20:
        return 2
    elif n < 100:
        return 20 + countDigitOne(n % 10) + countDigitOne(n // 10)
    elif n < 200:
        return 20 + 10 * countDigitOne(n % 100) + countDigitOne(n // 100)
    elif n < 1000:
        return 300 + countDigitOne(n % 100) + countDigitOne(n // 100)
    elif n < 2000:
        return 300 + 100 * countDigitOne(n % 1000) + countDigitOne(n // 1000)
    elif n < 10000:
        return 4000 + countDigitOne(n % 1000) + countDigitOne(n // 1000)
    elif n < 20000:
        return 4000 + 1000 * countDigitOne(n % 10000) + countDigitOne(n // 10000)
    elif n < 100000:
        return 50000 + countDigitOne(n % 10000) + countDigitOne(n // 10000)
    elif n < 200000:
        return 50000 + 10000 * countDigitOne(n % 100000) + countDigitOne(n // 100000)
    elif n < 1000000:
        return 600000 + countDigitOne(n % 100000) + countDigitOne(n // 100000)
    elif n < 2000000:
        return 600000 + 100000 * countDigitOne(n % 1000000) + countDigitOne(n // 1000000)
    elif n < 10000000:
        return 7000000 + countDigitOne(n % 1000000) + countDigitOne(n // 1000000)
    elif n < 20000000:
        return 7000000 + 1000000 * countDigitOne(n % 10000000) + countDigitOne(n // 10000000)
    elif n < 100000000:
        return 80000000 + countDigitOne(n % 100

=======
Suggestion 9

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # count the number of 1s in each digit
    # 1. 1s in the ones digit: 1, 11, 21, 31, ... 11(n/10), 1(n/10+1)
    # 2. 1s in the tens digit: 10, 11, 12, ... 19, 110, 111, ... 119, 210, 211, ... 219, 310, 311, ... 319, ... 11(n/100), 1(n/100+1)
    # 3. 1s in the hundreds digit: 100, 101, 102, ... 199, 1100, 1101, 1102, ... 1199, 2100, 2101, ... 2199, 3100, 3101, ... 3199, ... 11(n/1000), 1(n/1000+1)
    # ...
    # 4. 1s in the thousands digit: 1000, 1001, 1002, ... 1999, 11000, 11001, 11002, ... 11999, 21000, 21001, ... 21999, 31000, 31001, ... 31999, ... 11(n/10000), 1(n/10000+1)
    # ...
    # 5. 1s in the ten thousands digit: 10000, 10001, 10002, ... 19999, 110000, 110001, 110002, ... 119999, 210000, 210001, ... 219999, 310000, 310001, ... 319999, ... 11(n/100000), 1(n/100000+1)
    # ...
    # 6. 1s in the hundred thousands digit: 100000, 100001, 100002, ... 199999, 1100000, 1100001, 1100002, ... 1199999, 2100000, 2100001, ... 2199999, 3100000, 3100001,

=======
Suggestion 10

def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1000))
