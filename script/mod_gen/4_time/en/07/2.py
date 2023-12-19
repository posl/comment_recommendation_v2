def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [0] * n
    ugly[0] = 1
    index = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float("inf")
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[index[j]]:
                index[j] += 1
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()