def nthSuperUglyNumber(n, primes):
    ugly = [1]
    def gen(prime):
        for u in ugly:
            yield u * prime
    merged = heapq.merge(*map(gen, primes))
    while len(ugly) < n:
        u = next(merged)
        if u != ugly[-1]:
            ugly.append(u)
    return ugly[-1]
print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
