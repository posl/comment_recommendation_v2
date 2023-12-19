def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    primes.sort()
    uglies = [1]
    idxs = [0] * len(primes)
    while len(uglies) < n:
        next_ugly = min([primes[i] * uglies[idxs[i]] for i in range(len(primes))])
        uglies.append(next_ugly)
        for i in range(len(primes)):
            if primes[i] * uglies[idxs[i]] == next_ugly:
                idxs[i] += 1
    return uglies[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()