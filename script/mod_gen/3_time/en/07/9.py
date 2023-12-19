def nthSuperUglyNumber(n, primes):
    ugly = [1] * n
    idx = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = min([ugly[idx[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[i] == ugly[idx[j]] * primes[j]:
                idx[j] += 1
    return ugly[-1]
n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
