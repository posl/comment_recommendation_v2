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
