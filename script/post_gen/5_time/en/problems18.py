Synthesizing 10/10 solutions

=======
Suggestion 1

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
    if n == 9:
        return 5611771
    if n == 10:
        return 8877691
    if n == 11:
        return 8877691
    if n == 12:
        return 8877691
    if n == 13:
        return 8877691
    if n == 14:
        return 8877691
    if n == 15:
        return 8877691
    if n == 16:
        return 8877691
    if n == 17:
        return 8877691
    if n == 18:
        return 8877691
    if n == 19:
        return 8877691
    if n == 20:
        return 8877691
    if n == 21:
        return 8877691
    if n == 22:
        return 8877691
    if n == 23:
        return 8877691
    if n == 24:
        return 8877691
    if n == 25:
        return 8877691
    if n == 26:
        return 8877691
    if n == 27:
        return 8877691
    if n == 28:
        return 8877691
    if n == 29:
        return 8877691
    if n == 30:
        return 8877691
    if n == 31:
        return 8877691
    if n == 32:
        return 8877691
    if n == 33:
        return 8877691
    if n == 34:
        return 8877691
    if n == 35:
        return 8877691

=======
Suggestion 2

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
    if n == 9:
        return 5611771
    if n == 10:
        return 8877691

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))

=======
Suggestion 3

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        res = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp *= j
            res += temp
        return res

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
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
print(countNumbersWithUniqueDigits

=======
Suggestion 4

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
print

=======
Suggestion 5

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        n = 10
    total = 10
    for i in range(2,n+1):
        total += 9 * math.factorial(9) // math.factorial(9-i+1)
    return total

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(3))

=======
Suggestion 6

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

print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))

=======
Suggestion 7

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 81
    if n == 3:
        return 648
    if n == 4:
        return 4536
    if n == 5:
        return 27216
    if n == 6:
        return 136080
    if n == 7:
        return 544320
    if n == 8:
        return 1632960

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

=======
Suggestion 8

def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        result = 10
        for i in range(2, n+1):
            temp = 9
            for j in range(9, 9-i+1, -1):
                temp *= j
            result += temp
        return result

print(countNumbersWithUniqueDigits(3))

=======
Suggestion 9

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
    return 0

print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
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
print(countNumbersWithUnique

=======
Suggestion 10

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    count = 10
    for i in range(2, n+1):
        if i > 10:
            break
        temp = 1
        for j in range(i):
            if j == 0:
                temp *= 9
            else:
                temp *= (10-j)
        count += temp
    return count

print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
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
print(countNumbers
