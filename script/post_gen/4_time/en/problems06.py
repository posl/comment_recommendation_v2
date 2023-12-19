Synthesizing 10/10 solutions

=======
Suggestion 1

def nthUglyNumber(n):
    # 1 is always an ugly number
    ugly = [1]
    # keep track of the last index of each ugly number
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        # get the next ugly number by multiplying the minimum of the ugly numbers at the current indices
        # by the corresponding prime
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        # check if the ugly number at the current index is a multiple of the corresponding prime
        # if so, increment the index
        if ugly[-1] == ugly[i2] * 2:
            i2 += 1
        if ugly[-1] == ugly[i3] * 3:
            i3 += 1
        if ugly[-1] == ugly[i5] * 5:
            i5 += 1
        n -= 1
    return ugly[-1]

=======
Suggestion 2

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
        ugly.append(min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5))
    return ugly[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))

=======
Suggestion 3

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

n = 10
print(nthUglyNumber(n))

=======
Suggestion 4

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
Suggestion 5

def ugly_number(n):
    if n == 1:
        return 1
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for l in range(1, n):
        ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]

print(ugly_number(10))
print(ugly_number(1))

=======
Suggestion 6

def nthUglyNumber(n):
    ugly_numbers = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly_numbers) < n:
        next2 = ugly_numbers[i2] * 2
        next3 = ugly_numbers[i3] * 3
        next5 = ugly_numbers[i5] * 5
        next_ugly = min(next2, next3, next5)
        ugly_numbers.append(next_ugly)
        if next_ugly == next2:
            i2 += 1
        if next_ugly == next3:
            i3 += 1
        if next_ugly == next5:
            i5 += 1
    return ugly_numbers[-1]

print(nthUglyNumber(10))
print(nthUglyNumber(1))
print(nthUglyNumber(10))
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
print(nthUglyNumber(41))
print(nthUglyNumber(42))
print(nthUglyNumber(43))
print(nthUglyNumber(44))
print(n

=======
Suggestion 7

def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

=======
Suggestion 8

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
