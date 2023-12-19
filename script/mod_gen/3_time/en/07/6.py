def nthSuperUglyNumber(n, primes):
    ugly = [1]
    def gen(prime):
        for u in ugly:
            yield u * prime
    gens = map(gen, primes)
    merged = heapq.merge(*gens)
    while len(ugly) < n:
        next = next(merged)
        if next != ugly[-1]:
            ugly.append(next)
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()