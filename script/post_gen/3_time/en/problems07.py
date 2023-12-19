Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    i = 1
    while i < n:
        ugly.append(min([ugly[j] * primes[j] for j in range(len(primes))]))
        for j in range(len(primes)):
            if ugly[-1] == ugly[j] * primes[j]:
                primes[j] = primes[j] * ugly[j]
        i += 1
    return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp = [1] * n
    index = [0] * len(primes)
    for i in range(1, n):
        dp[i] = min([dp[index[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if dp[i] == dp[index[j]] * primes[j]:
                index[j] += 1
    return dp[-1]

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))

=======
Suggestion 3

def superUglyNumber(n, primes):
    ugly = [1]
    pri = {i:0 for i in primes}
    while len(ugly) < n:
        cand = min([ugly[pri[i]]*i for i in primes])
        ugly.append(cand)
        for i in primes:
            if cand == ugly[pri[i]]*i:
                pri[i] +=1
    return ugly[-1]

print(superUglyNumber(12, [2,7,13,19]))
print(superUglyNumber(1, [2,3,5]))
print(superUglyNumber(100000, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]))

=======
Suggestion 4

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    import heapq
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]

=======
Suggestion 5

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [0] * n
    ugly[0] = 1
    i = len(primes)
    index = [0] * i
    for j in range(1, n):
        ugly[j] = min([ugly[index[k]] * primes[k] for k in range(i)])
        for k in range(i):
            if ugly[j] == ugly[index[k]] * primes[k]:
                index[k] += 1
    return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
n = 1
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,

=======
Suggestion 7

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    def gen(prime):
        for u in ugly:
            yield u * prime
    gens = map(gen, primes)
    merged = heapq.merge(*gens)
    while len(ugly) < n:
        next = next(merged)
        if next != ugly[-1]:
            ugly.append(next)
    return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    for k in range(1, n):
        ugly[k] = min([primes[j] * ugly[i[j]] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[k] == primes[j] * ugly[i[j]]:
                i[j] += 1
    return ugly[-1]

=======
Suggestion 9

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if primes[j] * ugly[idx[j]] == ugly[i]:
                idx[j] += 1
    return ugly[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))

=======
Suggestion 10

def nthSuperUglyNumber(n, primes):
    ugly = [1] * n
    idx = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = min([ugly[idx[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[i] == ugly[idx[j]] * primes[j]:
                idx[j] += 1
    return ugly[-1]

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
