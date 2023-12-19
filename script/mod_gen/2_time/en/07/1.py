def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if primes[j] * ugly[idx[j]] == ugly[i]:
                idx[j] += 1
    return ugly[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(100000, [2,3,5]))
print(nthSuperUglyNumber(100000, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]))
