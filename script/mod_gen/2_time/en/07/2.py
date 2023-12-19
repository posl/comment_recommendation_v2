def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
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
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(15, [2,3,5]))
print(nthSuperUglyNumber(20, [2,3,5]))
print(nthSuperUglyNumber(25, [2,3,5]))
print(nthSuperUglyNumber(30, [2,3,5]))
print(nthSuperUglyNumber(35, [2,3,5]))
print(nthSuperUglyNumber(40, [2,3,5]))
print(nthSuperUglyNumber(45, [2,3,5]))
print(nthSuperUglyNumber(50, [2,3,5]))
print(nthSuperUglyNumber(55, [2,3,5]))
print(nthSuperUglyNumber(60, [2,3,5]))
print(nthSuperUglyNumber(65, [2,3,5]))
print(nthSuperUglyNumber(70, [2,3,5]))
print(nthSuperUglyNumber(75, [2,3,5]))
print(nthSuperUglyNumber(80, [2,3,5]))
print(nthSuperUglyNumber(85, [2,3,5]))
print(nthSuperUglyNumber(90, [2,3,5]))
print(nthSuperUglyNumber(95, [2,3,5]))
print(nthSuperUglyNumber(100, [2,3,5]))
print(nthSuperUglyNumber(105, [2,3,5]))
print(nthSuperUgly

if __name__ == '__main__':
    nthSuperUglyNumber()