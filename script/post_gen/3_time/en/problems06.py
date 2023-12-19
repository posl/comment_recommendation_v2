Synthesizing 10/10 solutions

=======
Suggestion 1

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
print(nthUglyNumber(1723))
print(nthUglyNumber(172

=======
Suggestion 2

def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        if ugly[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5

    return ugly[-1]

=======
Suggestion 3

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
Suggestion 4

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
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

=======
Suggestion 5

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
print(nthUglyNumber(39))
print(nthUglyNumber(40))

=======
Suggestion 6

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for i in range(1, n):
        ugly[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        if ugly[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(1690))

=======
Suggestion 7

def nthUglyNumber(n):
    ugly = [0] * n  # To store ugly numbers
    # 1 is the first ugly number
    ugly[0] = 1
    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 = i5 = 0
    # set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    # start loop to find value from ugly[1] to ugly[n]
    for l in range(1, n):
        # choose the min value of all available multiples
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        # increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    # return ugly[n] value
    return ugly[-1]

=======
Suggestion 8

def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))

=======
Suggestion 9

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
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

=======
Suggestion 10

def nthUglyNumber(n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

print(nthUglyNumber(10)) #12
print(nthUglyNumber(1)) #1
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber(1600)) #1399680000
print(nthUglyNumber(100)) #1536
print(nthUglyNumber(50)) #243
print(nthUglyNumber(20)) #36
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber(1690)) #2123366400
print(nthUglyNumber
