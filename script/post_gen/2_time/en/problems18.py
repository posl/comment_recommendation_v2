Synthesizing 10/10 solutions

=======
Suggestion 1

def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1

    res = 10
    uniqueDigits = 9
    availableNumber = 9
    while n > 1 and availableNumber > 0:
        uniqueDigits = uniqueDigits * availableNumber
        res += uniqueDigits
        availableNumber -= 1
        n -= 1

    return res

=======
Suggestion 2

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n == 2:
        return 91

    res = 91
    for i in range(3, n+1):
        res += 9*9*10**(i-2)
    return res

=======
Suggestion 3

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return 0
    count = 10
    for i in range(2, n + 1):
        temp = 9
        for j in range(0, i - 1):
            temp *= (9 - j)
        count += temp
    return count

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(0))
print(countNumbersWithUniqueDigits(1))
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
print(countNumbersWithUniqueDigits(48))
print(countNumbersWithUniqueDigits

=======
Suggestion 4

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
Suggestion 5

def uniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return 0
    count = 0
    for i in range(10**n):
        if len(str(i)) == len(set(str(i))):
            count += 1
    return count

print(uniqueDigits(2))
print(uniqueDigits(0))
print(uniqueDigits(1))
print(uniqueDigits(3))
print(uniqueDigits(4))
print(uniqueDigits(5))
print(uniqueDigits(6))
print(uniqueDigits(7))
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

=======
Suggestion 6

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        ans = 10
        for i in range(2, n+1):
            product = 9
            for j in range(9, 9-i+1, -1):
                product *= j
            ans += product
        return ans

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

=======
Suggestion 7

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

print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(4))
print(countNumbersWithUniqueDigits(5))
print(countNumbersWithUniqueDigits(6))
print(countNumbersWithUniqueDigits(7))
print(countNumbersWithUniqueDigits(8))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))

=======
Suggestion 8

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        count = 91
        for i in range(3, n+1):
            count += 9 * (10 - i + 1) * (10 - i + 1)
        return count

print(countNumbersWithUniqueDigits(3))

=======
Suggestion 9

def countNumbersWithUniqueDigits(n):
    if n==0:
        return 1
    if n==1:
        return 10
    if n==2:
        return 91
    if n>2:
        ans=91
        for i in range(3,n+1):
            ans+=(9*permutation(9,i-1))
        return ans

=======
Suggestion 10

def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        n = 10
    arr = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, n):
        arr[i] *= arr[i-1]
    return sum(arr) + 1

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
print(countNumbersWithUniqueDigits(
