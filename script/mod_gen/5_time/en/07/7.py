def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    uglies = [0] * n
    uglies[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        uglies[i] = min([primes[j] * uglies[idx[j]] for j in range(len(primes))])
        for j in range(len(primes)):
            if uglies[i] == primes[j] * uglies[idx[j]]:
                idx[j] += 1
    return uglies[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(10, [2,3,5]))
print(nthSuperUglyNumber(11, [2,3,5]))
print(nthSuperUglyNumber(12, [2,3,5]))
print(nthSuperUglyNumber(13, [2,3,5]))
print(nthSuperUglyNumber(14, [2,3,5]))
print(nthSuperUglyNumber(15, [2,3,5]))
print(nthSuperUglyNumber(16, [2,3,5]))
print(nthSuperUglyNumber(17, [2,3,5]))
print(nthSuperUglyNumber(18, [2,3,5]))
print(nthSuperUglyNumber(19, [2,3,5]))
print(nthSuperUglyNumber(20, [2,3,5]))
print(nthSuperUglyNumber(21, [2,3,5]))
print(nthSuperUglyNumber(22, [2,3,5]))
print(nthSuperUglyNumber(23, [2,3,5]))
print(nthSuperUglyNumber(24, [2,3,5]))
print(nthSuperUglyNumber(25, [2,3,5]))
print(nthSuperUglyNumber(26, [2,3,5]))
print(nthSuperUglyNumber(27, [2,3,5]))
print(nthSuperUglyNumber(28, [2,3,5
