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

if __name__ == '__main__':
    nthSuperUglyNumber()