def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
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

if __name__ == '__main__':
    nthSuperUglyNumber()