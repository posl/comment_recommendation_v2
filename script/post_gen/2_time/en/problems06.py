Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthUglyNumber(n):
    ugly = [0] * n # To store ugly numbers
    ugly[0] = 1

    # i2, i3, i5 will indicate indices for 2,3,5 respectively
    i2 = i3 =i5 = 0

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

    return ugly[-1]

print(nthUglyNumber(10)) #12
print(nthUglyNumber(1)) #1
print(nthUglyNumber(2)) #2
print(nthUglyNumber(3)) #3
print(nthUglyNumber(4)) #4
print(nthUglyNumber(5)) #5
print(nthUglyNumber(6)) #6
print(nthUglyNumber(7)) #8
print(nthUglyNumber(8)) #9
print(nthUglyNumber(9)) #10
print(nthUglyNumber(11)) #15
print(nthUglyNumber(12)) #16
print(nthUglyNumber(13)) #18
print(nthUglyNumber(14)) #20
print(nthUglyNumber(15)) #24
print(nthUglyNumber(16)) #25
print(nthUglyNumber(17)) #27
print(nthUglyNumber(18)) #30
print(nthUgly

=======
Suggestion 2

def checkUgly(n):
    while(n%2 == 0):
        n = n/2
    while(n%3 == 0):
        n = n/3
    while(n%5 == 0):
        n = n/5
    if(n == 1):
        return True
    else:
        return False

=======
Suggestion 3

def nthUglyNumber(n):
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

=======
Suggestion 4

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
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
Suggestion 5

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
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
print(nthUglyNumber(100))

=======
Suggestion 6

def nthUglyNumber(n):
    if n == 1:
        return 1
    ugly = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    while n > 1:
        u2 = ugly[i2] * 2
        u3 = ugly[i3] * 3
        u5 = ugly[i5] * 5
        umin = min(u2, u3, u5)
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
Suggestion 7

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
Suggestion 8

def nthUglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    for i in range(1, n):
        ugly[i] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        if ugly[i] == ugly[i2] * 2:
            i2 += 1
        if ugly[i] == ugly[i3] * 3:
            i3 += 1
        if ugly[i] == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]

print(nthUglyNumber(10))

=======
Suggestion 9

def nthUglyNumber(self, n: int) -> int:
    if n <= 0:
        return 0
    ugly = [1] * n
    i2 = i3 = i5 = -1
    x = v2 = v3 = v5 = 1
    for k in range(n):
        x = min(v2, v3, v5)
        ugly[k] = x
        if x == v2:
            i2 += 1
            v2 = ugly[i2] * 2
        if x == v3:
            i3 += 1
            v3 = ugly[i3] * 3
        if x == v5:
            i5 += 1
            v5 = ugly[i5] * 5
    return x
