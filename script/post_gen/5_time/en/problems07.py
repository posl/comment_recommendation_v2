Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1]
    index = [0] * len(primes)
    for i in range(n - 1):
        ugly.append(min([ugly[index[j]] * primes[j] for j in range(len(primes))]))
        for j in range(len(primes)):
            if ugly[-1] == ugly[index[j]] * primes[j]:
                index[j] += 1
    return ugly[-1]

=======
Suggestion 2

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

=======
Suggestion 3

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1]
    i = 0
    j = 0
    while len(ugly) < n:
        ugly.append(min(ugly[i]*primes[j], ugly[i+1]*primes[j+1]))
        if ugly[-1] == ugly[i]*primes[j]:
            i += 1
        if ugly[-1] == ugly[i+1]*primes[j+1]:
            j += 1
    return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    prime_index = [0] * len(primes)
    prime_factors = primes
    for i in range(1, n):
        ugly[i] = min(prime_factors)
        for j in range(len(primes)):
            if ugly[i] == prime_factors[j]:
                prime_index[j] += 1
                prime_factors[j] = primes[j] * ugly[prime_index[j]]
    return ugly[-1]

=======
Suggestion 5

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    primes.sort()
    uglies = [1]
    idxs = [0] * len(primes)
    while len(uglies) < n:
        next_ugly = min([primes[i] * uglies[idxs[i]] for i in range(len(primes))])
        uglies.append(next_ugly)
        for i in range(len(primes)):
            if primes[i] * uglies[idxs[i]] == next_ugly:
                idxs[i] += 1
    return uglies[-1]

=======
Suggestion 6

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    # 1. create a list of size n to store the super ugly numbers
    # 2. create a list of size m to store the indexes of numbers to multiply by primes
    # 3. create a list of size m to store the products of numbers multiplied by primes
    # 4. create a list of size m to store the products of numbers multiplied by primes
    # 5. move the index of the smallest product to the next index
    # 6. append the smallest product to the list of super ugly numbers
    # 7. return the last element in the list of super ugly numbers
    ugly_numbers = [1]
    k = len(primes)
    indexes = [0] * k
    products = [0] * k
    for i in range(1, n):
        for j in range(k):
            products[j] = ugly_numbers[indexes[j]] * primes[j]
        ugly_numbers.append(min(products))
        for j in range(k):
            if ugly_numbers[-1] == products[j]:
                indexes[j] += 1
    return ugly_numbers[-1]

=======
Suggestion 7

def nthSuperUglyNumber(n, primes):
    ugly=[1]
    idx=[0]*len(primes)
    for i in range(n-1):
        ugly.append(min([ugly[idx[j]]*primes[j] for j in range(len(primes))]))
        for j in range(len(primes)):
            if ugly[-1]==ugly[idx[j]]*primes[j]:
                idx[j]+=1
    return ugly[-1]

print(nthSuperUglyNumber(12,[2,7,13,19]))
print(nthSuperUglyNumber(1,[2,3,5]))

=======
Suggestion 8

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    uglies = [0] * n
    uglies[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        uglies[i] = min([primes[j] * uglies[idx[j]] for j in range(len(primes))])
        for j in range(len(primes)):
            if uglies[i] == primes[j] * uglies[idx[j]]:
                idx[j] += 1
    return uglies[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(10, [2,3,5]))
print(nthSuperUglyNumber(11, [2,3,5]))
print(nthSuperUglyNumber(12, [2,3,5]))
print(nthSuperUglyNumber(13, [2,3,5]))
print(nthSuperUglyNumber(14, [2,3,5]))
print(nthSuperUglyNumber(15, [2,3,5]))
print(nthSuperUglyNumber(16, [2,3,5]))
print(nthSuperUglyNumber(17, [2,3,5]))
print(nthSuperUglyNumber(18, [2,3,5]))
print(nthSuperUglyNumber(19, [2,3,5]))
print(nthSuperUglyNumber(20, [2,3,5]))
print(nthSuperUglyNumber(21, [2,3,5]))
print(nthSuperUglyNumber(22, [2,3,5]))
print(nthSuperUglyNumber(23, [2,3,5]))
print(nthSuperUglyNumber(24, [2,3,5]))
print(nthSuperUglyNumber(25, [2,3,5]))
print(nthSuperUglyNumber(26, [2,3,5]))
print(nthSuperUglyNumber(27, [2,3,5]))
print(nthSuperUglyNumber(28, [2,3,5

=======
Suggestion 9

def nthSuperUglyNumber(n, primes):
    ugly = [1]
    i = 1
    while len(ugly) < n:
        i += 1
        for p in primes:
            if i % p == 0:
                ugly.append(i)
                break
    return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 1
    primeCount = [0] * len(primes)
    for i in range(1,n):
        minVal = float('inf')
        for j in range(len(primes)):
            minVal = min(minVal, primes[j] * dp[primeCount[j]])
        dp[i] = minVal
        for j in range(len(primes)):
            if minVal == primes[j] * dp[primeCount[j]]:
                primeCount[j] += 1
    return dp[-1]
