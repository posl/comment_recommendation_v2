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
