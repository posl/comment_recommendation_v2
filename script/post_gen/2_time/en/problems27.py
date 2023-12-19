Synthesizing 10/10 solutions

=======
Suggestion 1

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    #for i in range(1, n+1):
    #    print(i)
    #    print(str(i).count('1'))
    #return sum([str(i).count('1') for i in range(1, n+1)])
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
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
print

=======
Suggestion 2

def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

=======
Suggestion 3

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0

    num = n
    base = 1
    total = 0

    while num > 0:
        last = num % 10
        num = num // 10

        total += num * base

        if last == 1:
            total += n % base + 1
        elif last > 1:
            total += base

        base *= 10

    return total

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
print(countDigitOne(10000000000))
print(countDigitOne(100000000000))
print(countDigitOne(1000000000000))
print(countDigitOne(10000000000000))
print(countDigitOne(100000000000000))
print(countDigitOne(1000000000000000))
print(countDigitOne(10000000000000000))
print(countDigitOne(100000000000000000))
print(countDigitOne(1000000000000000000))
print(countDigitOne(10000000000000000000))
print(countDigitOne(100000000000000000000))
print(countDigitOne(1000000000000000000000))
print(countDigitOne(10000000000000000000000))
print(countDigitOne(100000000000000000000000))
print(countDigitOne(1000000000000000000000000))
print(countDigitOne(10000000000000000000000000))
print(countDigitOne(100000000000000000000000000))
print(countDigitOne(1000000000000000000000000000))
print(countDigitOne(10000000000000000000000000000))
print(countDigitOne(100000000000000000000000000000))
print(countDigitOne(1000000000000000000000000000000))
print(countDigitOne(100000000000000000

=======
Suggestion 4

def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(13))
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
print(countDigitOne(72))
print

=======
Suggestion 5

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1,n+1):
        count += str(i).count('1')
    return count

countDigitOne(13)

=======
Suggestion 6

def number_of_1s(n):
    result = 0
    for i in range(1, n+1):
        result += str(i).count('1')
    return result

print(number_of_1s(13))
print(number_of_1s(0))
print(number_of_1s(1))
print(number_of_1s(2))
print(number_of_1s(10))
print(number_of_1s(11))
print(number_of_1s(12))
print(number_of_1s(13))
print(number_of_1s(14))
print(number_of_1s(15))
print(number_of_1s(16))
print(number_of_1s(17))
print(number_of_1s(18))
print(number_of_1s(19))
print(number_of_1s(20))
print(number_of_1s(21))
print(number_of_1s(22))
print(number_of_1s(23))
print(number_of_1s(24))
print(number_of_1s(25))
print(number_of_1s(26))
print(number_of_1s(27))
print(number_of_1s(28))
print(number_of_1s(29))
print(number_of_1s(30))
print(number_of_1s(31))
print(number_of_1s(32))
print(number_of_1s(33))
print(number_of_1s(34))
print(number_of_1s(35))
print(number_of_1s(36))
print(number_of_1s(37))
print(number_of_1s(38))
print(number_of_1s(39))
print(number_of_1s(40))
print(number_of_1s(41))
print(number_of_1s(42))
print(number_of_1s(43))
print(number_of_1s(44))
print(number_of_1s(45))
print(number_of_1s(46))
print(number_of_1s(47))
print(number_of_1s(48))
print(number_of_1s(49))
print(number_of_1s(50))
print(number_of_1s(51))
print(number_of_1s(52))
print(number_of_1s(53))
print(number_of_1s(54))
print(number_of_1s(55))
print(number_of_1s(56))
print(number

=======
Suggestion 7

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n < 20:
        return 2
    if n < 100:
        return 20 + countDigitOne(n % 10) + (n // 10 - 2) * 10
    if n < 200:
        return 20 + countDigitOne(n % 100) + (n // 100 - 1) * 100
    if n < 1000:
        return 300 + countDigitOne(n % 100) + (n // 100 - 3) * 100
    if n < 2000:
        return 300 + countDigitOne(n % 1000) + (n // 1000 - 1) * 1000
    if n < 10000:
        return 4000 + countDigitOne(n % 1000) + (n // 1000 - 4) * 1000
    if n < 20000:
        return 4000 + countDigitOne(n % 10000) + (n // 10000 - 1) * 10000
    if n < 100000:
        return 50000 + countDigitOne(n % 10000) + (n // 10000 - 5) * 10000
    if n < 200000:
        return 50000 + countDigitOne(n % 100000) + (n // 100000 - 1) * 100000
    if n < 1000000:
        return 600000 + countDigitOne(n % 100000) + (n // 100000 - 6) * 100000
    if n < 2000000:
        return 600000 + countDigitOne(n % 1000000) + (n // 1000000 - 1) * 1000000
    if n < 10000000:
        return 7000000 + countDigitOne(n % 1000000) + (n // 1000000 - 7) * 1000000
    if n < 20000000:
        return 7000000 + countDigit

=======
Suggestion 8

def count_digit_one(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n == 10:
        return 2
    if n == 11:
        return 4
    if n < 20:
        return 4 + count_digit_one(n - 10)
    if n < 100:
        return 10 + 2 * count_digit_one(n - 10)
    if n < 1000:
        return 300 + 2 * count_digit_one(n - 100)
    if n < 2000:
        return 400 + 3 * count_digit_one(n - 1000)
    if n < 10000:
        return 4000 + 4 * count_digit_one(n - 1000)
    if n < 20000:
        return 5000 + 5 * count_digit_one(n - 10000)
    if n < 100000:
        return 50000 + 5 * count_digit_one(n - 10000)
    if n < 200000:
        return 60000 + 6 * count_digit_one(n - 100000)
    if n < 1000000:
        return 600000 + 6 * count_digit_one(n - 100000)
    if n < 2000000:
        return 700000 + 7 * count_digit_one(n - 1000000)
    if n < 10000000:
        return 7000000 + 7 * count_digit_one(n - 1000000)
    if n < 20000000:
        return 8000000 + 8 * count_digit_one(n - 10000000)
    if n < 100000000:
        return 80000000 + 8 * count_digit_one(n - 10000000)
    if n < 200000000:
        return 90000000 + 9 * count_digit_one(n - 100000000)
    if n < 1000000000:
        return 900000000 + 9 * count_digit_one(n - 100000000)
    if n < 2000000000:
        return 1000000000 + 10 * count_digit_one(n - 1000000000)

=======
Suggestion 9

def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count

=======
Suggestion 10

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n >= 10 and n < 20:
        return n - 9
    if n >= 20 and n < 100:
        return 11 + countDigitOne(n % 10) + countDigitOne(n / 10)
    if n >= 100 and n < 1000:
        return 11 * (n / 100) + countDigitOne(n % 100) + countDigitOne(n / 100) * (n % 100 + 1)
    if n >= 1000 and n < 10000:
        return 11 * (n / 1000) + countDigitOne(n % 1000) + countDigitOne(n / 1000) * (n % 1000 + 1)
    if n >= 10000 and n < 100000:
        return 11 * (n / 10000) + countDigitOne(n % 10000) + countDigitOne(n / 10000) * (n % 10000 + 1)
    if n >= 100000 and n < 1000000:
        return 11 * (n / 100000) + countDigitOne(n % 100000) + countDigitOne(n / 100000) * (n % 100000 + 1)
    if n >= 1000000 and n < 10000000:
        return 11 * (n / 1000000) + countDigitOne(n % 1000000) + countDigitOne(n / 1000000) * (n % 1000000 + 1)
    if n >= 10000000 and n < 100000000:
        return 11 * (n / 10000000) + countDigitOne(n % 10000000) + countDigitOne(n / 10000000) * (n % 10000000 + 1)
    if n >= 100000000 and n < 1000000000:
        return 11 * (n / 100000000) + countDigitOne(n % 100000000) + countDigitOne(n / 100000000
