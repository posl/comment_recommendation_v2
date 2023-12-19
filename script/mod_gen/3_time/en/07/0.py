def nthSuperUglyNumber(n, primes):
    ugly = [1]
    i = 1
    while i < n:
        ugly.append(min([ugly[j] * primes[j] for j in range(len(primes))]))
        for j in range(len(primes)):
            if ugly[-1] == ugly[j] * primes[j]:
                primes[j] = primes[j] * ugly[j]
        i += 1
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()