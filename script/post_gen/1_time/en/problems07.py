Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    pointers = [0] * len(primes)
    for _ in range(1, n):
        next_ugly = min([ugly[pointers[i]] * primes[i] for i in range(len(primes))])
        ugly.append(next_ugly)
        for i in range(len(primes)):
            if ugly[pointers[i]] * primes[i] == next_ugly:
                pointers[i] += 1
    return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1

    for i in range(1, n):
        ugly[i] = float("inf")
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])

        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[idx[j]]:
                idx[j] += 1

    return ugly[-1]

=======
Suggestion 3

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    primes_index = [0] * len(primes)
    primes_value = primes.copy()
    for i in range(1, n):
        ugly[i] = min(primes_value)
        for j in range(len(primes)):
            if ugly[i] == primes_value[j]:
                primes_index[j] += 1
                primes_value[j] = ugly[primes_index[j]] * primes[j]
    return ugly[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(100000, [2, 3, 5]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]))
print(nthSuperUglyNumber(100000

=======
Suggestion 4

def superUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1]
    idx = [0] * len(primes)
    while len(ugly) < n:
        next = min(ugly[idx[i]] * primes[i] for i in range(len(primes)))
        ugly.append(next)
        for i in range(len(primes)):
            if ugly[idx[i]] * primes[i] == next:
                idx[i] += 1
    return ugly[-1]

print(superUglyNumber(12, [2,7,13,19]))
print(superUglyNumber(1, [2,3,5]))

=======
Suggestion 5

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    count = 1
    while count < n:
        min_val = float('inf')
        min_index = -1
        for j in range(len(primes)):
            if primes[j] * ugly[i[j]] < min_val:
                min_val = primes[j] * ugly[i[j]]
                min_index = j
            elif primes[j] * ugly[i[j]] == min_val:
                i[j] += 1
        if min_val != ugly[count - 1]:
            ugly[count] = min_val
            count += 1
        i[min_index] += 1
    return ugly[n - 1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))

=======
Suggestion 6

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = 1
    index = [0] * len(primes)
    while i < n:
        minUgly = float('inf')
        for j in range(len(primes)):
            minUgly = min(minUgly, primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if minUgly == primes[j] * ugly[index[j]]:
                index[j] += 1
        ugly[i] = minUgly
        i += 1
    return ugly[n-1]

=======
Suggestion 7

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    pointers = [0] * len(primes)
    while n > 1:
        candidates = [ugly[pointers[i]] * primes[i] for i in range(len(primes))]
        nextUgly = min(candidates)
        ugly.append(nextUgly)
        for i in range(len(primes)):
            if nextUgly == candidates[i]:
                pointers[i] += 1
        n -= 1
    return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[idx[j]]:
                idx[j] += 1
    return ugly[-1]

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))

=======
Suggestion 9

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    # i2, i3, i5 will indicate the indices for the current ugly number multiplied by 2, 3, 5 respectively
    i2, i3, i5 = 0, 0, 0
    # c2, c3, c5 will indicate the current ugly number multiplied by 2, 3, 5 respectively
    c2, c3, c5 = 2, 3, 5
    for i in range(1, n):
        # choose the next ugly number as the minimum of c2, c3, c5
        ugly.append(min(c2, c3, c5))
        # increment the index for the chosen ugly number
        if ugly[i] == c2:
            i2 += 1
            c2 = ugly[i2] * 2
        if ugly[i] == c3:
            i3 += 1
            c3 = ugly[i3] * 3
        if ugly[i] == c5:
            i5 += 1
            c5 = ugly[i5] * 5
    return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(n, primes):
    dp = [0] * n
    dp[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(len(primes)):
            dp[i] = min(dp[i], dp[idx[j]] * primes[j])
        for j in range(len(primes)):
            if dp[i] == dp[idx[j]] * primes[j]:
                idx[j] += 1
    return dp[-1]
