def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp = [1]
    idx = [0] * len(primes)
    while len(dp) < n:
        temp = []
        for i in range(len(primes)):
            temp.append(dp[idx[i]] * primes[i])
        m = min(temp)
        dp.append(m)
        for i in range(len(primes)):
            if m == temp[i]:
                idx[i] += 1
    return dp[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()