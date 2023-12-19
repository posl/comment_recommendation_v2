def nthSuperUglyNumber(n, primes):
    ugly = [1]
    i = 1
    while len(ugly) < n:
        i += 1
        for p in primes:
            if i % p == 0:
                ugly.append(i)
                break
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()