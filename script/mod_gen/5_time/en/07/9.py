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

if __name__ == '__main__':
    nthSuperUglyNumber()