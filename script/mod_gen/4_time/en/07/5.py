def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[idx[j]]:
                idx[j] += 1
    return ugly[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
