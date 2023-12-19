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

if __name__ == '__main__':
    nthSuperUglyNumber()