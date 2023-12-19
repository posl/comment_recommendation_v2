def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    prime_index = [0] * len(primes)
    prime_factors = primes
    for i in range(1, n):
        ugly[i] = min(prime_factors)
        for j in range(len(primes)):
            if ugly[i] == prime_factors[j]:
                prime_index[j] += 1
                prime_factors[j] = primes[j] * ugly[prime_index[j]]
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()