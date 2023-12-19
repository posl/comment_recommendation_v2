def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    index = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[index[j]]:
                index[j] += 1
    return ugly[-1]
primes = [2,7,13,19]
n = 12
print(nthSuperUglyNumber(n, primes))
