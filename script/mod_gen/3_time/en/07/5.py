def nthSuperUglyNumber(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]
n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
n = 1
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
print(nthSuperUglyNumber(n, primes))
n = 100000
primes = [2,3,5,7,11,13,17,19,

if __name__ == '__main__':
    nthSuperUglyNumber()