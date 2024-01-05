def nthSuperUglyNumber(n, primes):
    dp = [0] * n
    dp[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(len(primes)):
            dp[i] = min(dp[i], dp[idx[j]] * primes[j])
        for j in range(len(primes)):
            if dp[i] == dp[idx[j]] * primes[j]:
                idx[j] += 1
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = nthSuperUglyNumber(n, primes)
    print(a)