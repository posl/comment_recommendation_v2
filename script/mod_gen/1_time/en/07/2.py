def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    primes_index = [0] * len(primes)
    primes_value = primes.copy()
    for i in range(1, n):
        ugly[i] = min(primes_value)
        for j in range(len(primes)):
            if ugly[i] == primes_value[j]:
                primes_index[j] += 1
                primes_value[j] = ugly[primes_index[j]] * primes[j]
    return ugly[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(100000, [2, 3, 5]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]))
print(nthSuperUglyNumber(100000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]))
print(nthSuperUglyNumber(100000
