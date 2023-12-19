def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    for k in range(1, n):
        ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[k] == ugly[i[j]] * primes[j]:
                i[j] += 1
    return ugly[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
