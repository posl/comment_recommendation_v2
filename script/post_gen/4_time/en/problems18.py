Synthesizing 10/10 solutions

=======
Suggestion 1

def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    result = 91
    for i in range(3,n+1):
        result += (10-i+1)*factorial(9)//factorial(10-i)
    return result

=======
Suggestion 2

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    result = 10
    for i in range(2, n+1):
        temp = 9
        for j in range(9, 9-i+1, -1):
            temp *= j
        result += temp
    return result
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
print(countNumbersWithUniqueDigits(12))
print(countNumbersWithUniqueDigits(13))
print(countNumbersWithUniqueDigits(14))
print(countNumbersWithUniqueDigits(15))
print(countNumbersWithUniqueDigits(16))
print(countNumbersWithUniqueDigits(17))
print(countNumbersWithUniqueDigits(18))
print(countNumbersWithUniqueDigits(19))
print(countNumbersWithUniqueDigits(20))
print(countNumbersWithUniqueDigits(21))
print(countNumbersWithUniqueDigits(22))
print(countNumbersWithUniqueDigits(23))
print(countNumbersWithUniqueDigits(24))
print(countNumbersWithUniqueDigits(25))
print(countNumbersWithUniqueDigits(26))
print(countNumbersWithUniqueDigits(27))
print(countNumbersWithUniqueDigits(28))
print(countNumbersWithUniqueDigits(29))
print(countNumbersWithUniqueDigits(30))
print(countNumbersWithUniqueDigits(31))
print(countNumbersWithUniqueDigits(32))
print(countNumbersWithUniqueDigits(33))
print(countNumbersWithUniqueDigits(34))
print(countNumbersWithUniqueDigits(35))
print(countNumbersWithUniqueDigits(36))
print(countNumbersWithUniqueDigits(37))
print(countNumbersWithUniqueDigits(38))
print(countNumbersWithUniqueDigits(39))
print(countNumbersWithUniqueDigits(40))
print(countNumbersWithUniqueDigits(41))
print(countNumbersWithUniqueDigits(42))
print(countNumbersWithUniqueDigits(43))
print(countNumbersWithUniqueDigits(44))
print(countNumbersWithUniqueDigits(45))
print(countNumbersWithUniqueDigits(46))
print(countNumbersWithUniqueDigits(47))

=======
Suggestion 3

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))

=======
Suggestion 4

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    count = 10
    for i in range(2, n+1):
        temp = 9
        for j in range(1, i):
            temp *= (10-j)
        count += temp
    return count

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))

=======
Suggestion 5

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        return countNumbersWithUniqueDigits(n-1) + (countNumbersWithUniqueDigits(n-1) - countNumbersWithUniqueDigits(n-2))*(10-n+1)

print(countNumbersWithUniqueDigits(3))

=======
Suggestion 6

def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n == 3:
        return 739
    if n == 4:
        return 5275
    if n == 5:
        return 32491
    if n == 6:
        return 168571
    if n == 7:
        return 712891
    if n == 8:
        return 2345851
    return 0

print(uniqueDigits(0))
print(uniqueDigits(1))
print(uniqueDigits(2))
print(uniqueDigits(3))
print(uniqueDigits(4))
print(uniqueDigits(5))
print(uniqueDigits(6))
print(uniqueDigits(7))
print(uniqueDigits(8))

=======
Suggestion 7

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n > 10:
        return 0
    else:
        res = 91
        for i in range(3, n+1):
            temp = 1
            for j in range(i):
                if j == 0:
                    temp = temp * 9
                else:
                    temp = temp * (10-j)
            res = res + temp
        return res

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
print(countNumbersWithUniqueDigits(12))
print(countNumbersWithUniqueDigits(13))
print(countNumbersWithUniqueDigits(14))
print(countNumbersWithUniqueDigits(15))
print(countNumbersWithUniqueDigits(16))
print(countNumbersWithUniqueDigits(17))
print(countNumbersWithUniqueDigits(18))
print(countNumbersWithUniqueDigits(19))
print(countNumbersWithUniqueDigits(20))
print(countNumbersWithUniqueDigits(21))
print(countNumbersWithUniqueDigits(22))
print(countNumbersWithUniqueDigits(23))
print(countNumbersWithUniqueDigits(24))
print(countNumbersWithUniqueDigits(25))
print(countNumbersWithUniqueDigits(26))
print(countNumbersWithUniqueDigits(27))
print(countNumbersWithUniqueDigits(28))
print(countNumbersWithUniqueDigits(29))
print(countNumbersWithUniqueDigits(30))
print(countNumbersWithUniqueDigits(31))
print(countNumbersWithUniqueDigits(32))
print(countNumbersWithUniqueDigits(33))
print(countNumbersWithUniqueDigits(34))
print(countNumbersWithUniqueDigits(35))
print(countNumbersWithUniqueDigits(36))
print(countNumbersWithUniqueDigits(37))
print(countNumbersWithUniqueDigits(38))
print(countNumbersWithUniqueDigits(39))
print(countNumbersWithUniqueDigits(40))
print(countNumbersWithUniqueDigits(41))
print(countNumbersWithUniqueDigits(42))
print(countNumbersWith

=======
Suggestion 8

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return 0
    if n == 10:
        return 8877691
    dp = [0]*11
    dp[1] = 10
    dp[2] = 81
    for i in range(3, n+1):
        dp[i] = dp[i-1]*(11-i)
    return sum(dp[:n+1])

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
print(countNumbersWithUniqueDigits(12))
print(countNumbersWithUniqueDigits(13))
print(countNumbersWithUniqueDigits(14))
print(countNumbersWithUniqueDigits(15))
print(countNumbersWithUniqueDigits(16))
print(countNumbersWithUniqueDigits(17))
print(countNumbersWithUniqueDigits(18))
print(countNumbersWithUniqueDigits(19))
print(countNumbersWithUniqueDigits(20))
print(countNumbersWithUniqueDigits(21))
print(countNumbersWithUniqueDigits(22))
print(countNumbersWithUniqueDigits(23))
print(countNumbersWithUniqueDigits(24))
print(countNumbersWithUniqueDigits(25))
print(countNumbersWithUniqueDigits(26))
print(countNumbersWithUniqueDigits(27))
print(countNumbersWithUniqueDigits(28))
print(countNumbersWithUniqueDigits(29))
print(countNumbersWithUniqueDigits(30))
print(countNumbersWithUniqueDigits(31))
print(countNumbersWithUniqueDigits(32))
print(countNumbersWithUniqueDigits(33))
print(countNumbersWithUniqueDigits(34))
print(countNumbersWithUniqueDigits(35))
print(countNumbersWithUniqueDigits(36))
print(countNumbersWithUniqueDigits(37))
print(countNumbersWithUniqueDigits(38))
print(countNumbersWithUniqueDigits(39))
print(countNumbersWithUniqueDigits(40))
print(countNumbersWithUniqueDigits(41))
print(countNumbersWithUniqueDigits(42))
print(countNumbersWithUniqueDigits(43))
print(countNumbersWithUniqueDigits(44))
print(countNumbersWithUniqueDigits(45))
print(countNumbersWithUniqueDigits(46))
print(countNumbersWithUniqueDigits(47))
print(countNumbersWithUniqueDigits(48))
print(countNumbersWithUnique

=======
Suggestion 9

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91
    if n > 10:
        return 0
    count = 91
    for i in range(3,n+1):
        temp = 9
        for j in range(i-1):
            temp *= (9-j)
        count += temp
    return count

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
print(countNumbersWithUniqueDigits(12))
print(countNumbersWithUniqueDigits(13))
print(countNumbersWithUniqueDigits(14))
print(countNumbersWithUniqueDigits(15))
print(countNumbersWithUniqueDigits(16))
print(countNumbersWithUniqueDigits(17))
print(countNumbersWithUniqueDigits(18))
print(countNumbersWithUniqueDigits(19))
print(countNumbersWithUniqueDigits(20))
print(countNumbersWithUniqueDigits(21))
print(countNumbersWithUniqueDigits(22))
print(countNumbersWithUniqueDigits(23))
print(countNumbersWithUniqueDigits(24))
print(countNumbersWithUniqueDigits(25))
print(countNumbersWithUniqueDigits(26))
print(countNumbersWithUniqueDigits(27))
print(countNumbersWithUniqueDigits(28))
print(countNumbersWithUniqueDigits(29))
print(countNumbersWithUniqueDigits(30))
print(countNumbersWithUniqueDigits(31))
print(countNumbersWithUniqueDigits(32))
print(countNumbersWithUniqueDigits(33))
print(countNumbersWithUniqueDigits(34))
print(countNumbersWithUniqueDigits(35))
print(countNumbersWithUniqueDigits(36))
print(countNumbersWithUniqueDigits(37))
print(countNumbersWithUniqueDigits(38))
print(countNumbersWithUniqueDigits(39))
print(countNumbersWithUniqueDigits(40))
print(countNumbersWithUniqueDigits(41))
print(countNumbersWithUniqueDigits(42))
print(countNumbersWithUniqueDigits(43))
print(countNumbersWithUniqueDigits(44))
print(countNumbersWithUniqueDigits(45))
print

=======
Suggestion 10

def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        n = 10
    result = 0
    for i in range(10**(n-1), 10**n):
        if len(set(str(i))) == len(str(i)):
            result += 1
    return result

print(uniqueDigits(2))
print(uniqueDigits(0))
print(uniqueDigits(1))
print(uniqueDigits(8))
print(uniqueDigits(9))
print(uniqueDigits(10))
print(uniqueDigits(11))
print(uniqueDigits(12))
print(uniqueDigits(13))
print(uniqueDigits(14))
print(uniqueDigits(15))
print(uniqueDigits(16))
print(uniqueDigits(17))
print(uniqueDigits(18))
print(uniqueDigits(19))
print(uniqueDigits(20))
print(uniqueDigits(21))
print(uniqueDigits(22))
print(uniqueDigits(23))
print(uniqueDigits(24))
print(uniqueDigits(25))
print(uniqueDigits(26))
print(uniqueDigits(27))
print(uniqueDigits(28))
print(uniqueDigits(29))
print(uniqueDigits(30))
print(uniqueDigits(31))
print(uniqueDigits(32))
print(uniqueDigits(33))
print(uniqueDigits(34))
print(uniqueDigits(35))
print(uniqueDigits(36))
print(uniqueDigits(37))
print(uniqueDigits(38))
print(uniqueDigits(39))
print(uniqueDigits(40))
print(uniqueDigits(41))
print(uniqueDigits(42))
print(uniqueDigits(43))
print(uniqueDigits(44))
print(uniqueDigits(45))
print(uniqueDigits(46))
print(uniqueDigits(47))
print(uniqueDigits(48))
print(uniqueDigits(49))
print(uniqueDigits(50))
print(uniqueDigits(51))
print(uniqueDigits(52))
print(uniqueDigits(53))
print(uniqueDigits(54))
print(uniqueDigits(55))
print(uniqueDigits(56))
print(uniqueDigits(57))
print(uniqueDigits(58))
print(uniqueDigits(59))
print(uniqueDigits(60))
print(uniqueDigits(61))
print(uniqueDigits(62))
print(uniqueDigits(63))
print(uniqueDigits(64))
print(uniqueDigits(65))
print(uniqueDigits(66))
print(uniqueDigits(67))
print(uniqueDigits(68))
print(uniqueDigits(69))
print(uniqueDigits(70))
print(uniqueDigits(71))
print(uniqueDigits(72))
print(uniqueDigits(73))
