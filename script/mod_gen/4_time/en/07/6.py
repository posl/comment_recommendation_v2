def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
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
n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
n = 1
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
