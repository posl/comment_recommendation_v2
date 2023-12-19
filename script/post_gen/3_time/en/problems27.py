Synthesizing 10/10 solutions

=======
Suggestion 1

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
        return 20 + 10*(n-19) + countDigitOne(n-10*(n-19))
    if n < 200:
        return 20 + 10*(n-99) + countDigitOne(n-10*(n-99))
    if n < 1000:
        return 300 + 100*(n-199) + countDigitOne(n-100*(n-199))
    if n < 2000:
        return 300 + 100*(n-999) + countDigitOne(n-100*(n-999))
    if n < 10000:
        return 4000 + 1000*(n-1999) + countDigitOne(n-1000*(n-1999))
    if n < 20000:
        return 4000 + 1000*(n-9999) + countDigitOne(n-1000*(n-9999))
    if n < 100000:
        return 50000 + 10000*(n-19999) + countDigitOne(n-10000*(n-19999))
    if n < 200000:
        return 50000 + 10000*(n-99999) + countDigitOne(n-10000*(n-99999))
    if n < 1000000:
        return 600000 + 100000*(n-199999) + countDigitOne(n-100000*(n-199999))
    if n < 2000000:
        return 600000 + 100000*(n-999999) + countDigitOne(n-100000*(n-999999))
    if n < 10000000:
        return 7000000 + 1000000*(n-1999999) + countDigitOne(n-1000000*(n-1999999))
    if n < 20000000:
        return 7000000 + 1000000*(n-9999999) + countDigitOne(n-1000000*(n-9999999))
    if n < 100

=======
Suggestion 3

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # if n < 1, return 0
    if n < 1:
        return 0

    # if n < 10, return 1
    if n < 10:
        return 1

    # if n < 100, return 20
    if n < 100:
        if n < 20:
            return 1 + n - 10 + 1
        else:
            return 20

    # if n < 1000, return 300
    if n < 1000:
        if n < 200:
            return 1 + countDigitOne(n-100) + 100
        else:
            return 300

    # if n < 10000, return 4000
    if n < 10000:
        if n < 2000:
            return 1 + countDigitOne(n-1000) + 1000
        else:
            return 4000

    # if n < 100000, return 50000
    if n < 100000:
        if n < 20000:
            return 1 + countDigitOne(n-10000) + 10000
        else:
            return 50000

    # if n < 1000000, return 600000
    if n < 1000000:
        if n < 200000:
            return 1 + countDigitOne(n-100000) + 100000
        else:
            return 600000

    # if n < 10000000, return 7000000
    if n < 10000000:
        if n < 2000000:
            return 1 + countDigitOne(n-1000000) + 1000000
        else:
            return 7000000

    # if n < 100000000, return 80000000
    if n < 100000000:
        if n < 20000000:
            return 1 + countDigitOne(n-10000000) + 10000000
        else:
            return 80000000

    # if n < 1000000000, return 900000000
    if n < 1000000000:
        if n

=======
Suggestion 4

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
print(countDigitOne(

=======
Suggestion 5

def countDigitOne(n):
    if n <= 0:
        return 0
    if n < 10:
        return 1
    if n < 20:
        return 2
    if n < 100:
        return 20 + countDigitOne(n%10) + (n//10 - 2)*10
    if n < 1000:
        return 300 + countDigitOne(n%100) + (n//100 - 3)*100
    if n < 10000:
        return 4000 + countDigitOne(n%1000) + (n//1000 - 4)*1000
    if n < 100000:
        return 50000 + countDigitOne(n%10000) + (n//10000 - 5)*10000
    if n < 1000000:
        return 600000 + countDigitOne(n%100000) + (n//100000 - 6)*100000
    if n < 10000000:
        return 7000000 + countDigitOne(n%1000000) + (n//1000000 - 7)*1000000
    if n < 100000000:
        return 80000000 + countDigitOne(n%10000000) + (n//10000000 - 8)*10000000
    if n < 1000000000:
        return 900000000 + countDigitOne(n%100000000) + (n//100000000 - 9)*100000000
    if n == 1000000000:
        return 1000000000
    return 0

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
    # find the highest digit
    digit = 1
    while digit <= n:
        digit *= 10
    digit //= 10
    # find the number of 1s in the highest digit
    count = 0
    if n // digit == 1:
        count += n % digit + 1
    else:
        count += digit
    # find the number of 1s in the rest digits
    count += (n // digit) * countDigitOne(digit - 1)
    # find the number of 1s in the rest numbers
    count += countDigitOne(n % digit)
    return count

=======
Suggestion 7

def countDigitOne(n):
    count = 0
    for i in range(1,n+1):
        for j in str(i):
            if j == '1':
                count+=1
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(100))
print(countDigitOne(101))
print(countDigitOne(102))
print(countDigitOne(111))

=======
Suggestion 8

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
        return 20 + countDigitOne(n % 10)
    if n < 200:
        return 20 + countDigitOne(n % 100) + n % 100 + 1
    if n < 1000:
        return 300 + countDigitOne(n % 100)
    if n < 2000:
        return 300 + countDigitOne(n % 1000) + n % 1000 + 1
    if n < 10000:
        return 4000 + countDigitOne(n % 1000)
    if n < 20000:
        return 4000 + countDigitOne(n % 10000) + n % 10000 + 1
    if n < 100000:
        return 50000 + countDigitOne(n % 10000)
    if n < 200000:
        return 50000 + countDigitOne(n % 100000) + n % 100000 + 1
    if n < 1000000:
        return 600000 + countDigitOne(n % 100000)
    if n < 2000000:
        return 600000 + countDigitOne(n % 1000000) + n % 1000000 + 1
    if n < 10000000:
        return 7000000 + countDigitOne(n % 1000000)
    if n < 20000000:
        return 7000000 + countDigitOne(n % 10000000) + n % 10000000 + 1
    if n < 100000000:
        return 80000000 + countDigitOne(n % 10000000)
    if n < 200000000:
        return 80000000 + countDigitOne(n % 100000000) + n % 100000000 + 1
    if n < 1000000000:
        return 900000000 + countDigitOne(n % 100000000)
    if n < 2000000000:
        return 900000

=======
Suggestion 9

def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count

print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))

=======
Suggestion 10

def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    # 1 10 11 12 13 14 15 16 17 18 19 21 31 41 51 61 71 81 91 101 111 121 131 141 151 161 171 181 191 201 211 221 231 241 251 261 271 281 291 301 311 321 331 341 351 361 371 381 391 401 411 421 431 441 451 461 471 481 491 501 511 521 531 541 551 561 571 581 591 601 611 621 631 641 651 661 671 681 691 701 711 721 731 741 751 761 771 781 791 801 811 821 831 841 851 861 871 881 891 901 911 921 931 941 951 961 971 981 991 1001 1011 1021 1031 1041 1051 1061 1071 1081 1091 1101 1111 1121 1131 1141 1151 1161 1171 1181 1191 1201 1211 1221 1231 1241 1251 1261 1271 1281 1291 1301 1311 1321 1331 1341 1351 1361 1371 1381 1391 1401 1411 1421 1431 1441 1451 1461 1471 1481 1491 1501 1511 1521 1531 1541 1551 1561 1571 1581 1591 1601 1611 1621 1631 1641 1651 1661 1671 1681 1691 1701 1711 1721 1731 1741 1751 1761 1771 1781 1791 1801 1811 1821 1831 1841 1851
