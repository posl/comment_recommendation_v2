Synthesizing 10/10 solutions

=======
Suggestion 1

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    uglies = [1]
    i2 = i3 = i5 = 0
    while len(uglies) < n:
        while uglies[i2] * 2 <= uglies[-1]:
            i2 += 1
        while uglies[i3] * 3 <= uglies[-1]:
            i3 += 1
        while uglies[i5] * 5 <= uglies[-1]:
            i5 += 1
        uglies.append(min(uglies[i2] * 2, uglies[i3] * 3, uglies[i5] * 5))
    return uglies[-1]

=======
Suggestion 2

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))
print("The values above should be 12, 1, and 2123366400.")

=======
Suggestion 3

def nthUglyNumber(n):
    if n == 1:
        return 1
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5))
    return ugly[-1]

print(nthUglyNumber(10))

=======
Suggestion 4

def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))

=======
Suggestion 5

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

=======
Suggestion 6

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    ugly = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    for i in range(1, n):
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        if ugly[i] == ugly[i2] * 2:
            i2 += 1
        if ugly[i] == ugly[i3] * 3:
            i3 += 1
        if ugly[i] == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]

=======
Suggestion 7

def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))
print(nthUglyNumber(1691))
print(nthUglyNumber(1692))
print(nthUglyNumber(1693))
print(nthUglyNumber(1694))
print(nthUglyNumber(1695))
print(nthUglyNumber(1696))
print(nthUglyNumber(1697))
print(nthUglyNumber(1698))
print(nthUglyNumber(1699))
print(nthUglyNumber(1700))
print(nthUglyNumber(1701))
print(nthUglyNumber(1702))
print(nthUglyNumber(1703))
print(nthUglyNumber(1704))
print(nthUglyNumber(1705))
print(nthUglyNumber(1706))
print(nthUglyNumber(1707))
print(nthUglyNumber(1708))
print(nthUglyNumber(1709))
print(nthUglyNumber(1710))
print(nthUglyNumber(1711))
print(nthUglyNumber(1712))
print(nthUglyNumber(1713))
print(nthUglyNumber(1714))
print(nthUglyNumber(1715))
print(nthUglyNumber(1716))
print(nthUglyNumber(1717))
print(nthUglyNumber(1718))
print(nthUglyNumber(1719))
print(nthUglyNumber(1720))
print(nthUglyNumber(1721))
print(nthUglyNumber(1722))
print(nthUgly

=======
Suggestion 8

def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))
print(nthUglyNumber(2))
print(nthUglyNumber(3))
print(nthUglyNumber(4))
print(nthUglyNumber(5))
print(nthUglyNumber(6))
print(nthUglyNumber(7))
print(nthUglyNumber(8))
print(nthUglyNumber(9))
print(nthUglyNumber(11))
print(nthUglyNumber(12))
print(nthUglyNumber(13))
print(nthUglyNumber(14))
print(nthUglyNumber(15))
print(nthUglyNumber(16))
print(nthUglyNumber(17))
print(nthUglyNumber(18))
print(nthUglyNumber(19))
print(nthUglyNumber(20))
print(nthUglyNumber(21))
print(nthUglyNumber(22))
print(nthUglyNumber(23))
print(nthUglyNumber(24))
print(nthUglyNumber(25))
print(nthUglyNumber(26))
print(nthUglyNumber(27))
print(nthUglyNumber(28))
print(nthUglyNumber(29))
print(nthUglyNumber(30))
print(nthUglyNumber(31))
print(nthUglyNumber(32))
print(nthUglyNumber(33))
print(nthUglyNumber(34))
print(nthUglyNumber(35))
print(nthUglyNumber(36))
print(nthUglyNumber(37))
print(nthUglyNumber(38))
print(nthUglyNumber(39

=======
Suggestion 9

def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]:
            i2 += 1
        while ugly[i3] * 3 <= ugly[-1]:
            i3 += 1
        while ugly[i5] * 5 <= ugly[-1]:
            i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))

=======
Suggestion 10

def nthUglyNumber(n):
    # ugly numbers: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
    # prime factors: 2, 3, 5
    # n = 10 -> return 12
    # n = 1 -> return 1
    # n = 2 -> return 2
    # n = 3 -> return 3
    # n = 4 -> return 4
    # n = 5 -> return 5
    # n = 6 -> return 6
    # n = 7 -> return 8
    # n = 8 -> return 9
    # n = 9 -> return 10
    # n = 10 -> return 12
    # n = 11 -> return 15
    # n = 12 -> return 16
    # n = 13 -> return 18
    # n = 14 -> return 20
    # n = 15 -> return 24
    # n = 16 -> return 25
    # n = 17 -> return 27
    # n = 18 -> return 30
    # n = 19 -> return 32
    # n = 20 -> return 36
    # n = 21 -> return 40
    # n = 22 -> return 45
    # n = 23 -> return 48
    # n = 24 -> return 50
    # n = 25 -> return 54
    # n = 26 -> return 60
    # n = 27 -> return 64
    # n = 28 -> return 72
    # n = 29 -> return 75
    # n = 30 -> return 80
    # n = 31 -> return 81
    # n = 32 -> return 90
    # n = 33 -> return 96
    # n = 34 -> return 100
    # n = 35 -> return 108
    # n = 36 -> return 120
    # n = 37 -> return 125
    # n = 38 -> return 128
    # n = 39 -> return 135
    # n =
