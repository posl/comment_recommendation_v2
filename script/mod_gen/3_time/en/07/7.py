def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    for k in range(1, n):
        ugly[k] = min([primes[j] * ugly[i[j]] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[k] == primes[j] * ugly[i[j]]:
                i[j] += 1
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()