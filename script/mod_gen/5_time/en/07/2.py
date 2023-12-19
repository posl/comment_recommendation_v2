def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1]
    i = 0
    j = 0
    while len(ugly) < n:
        ugly.append(min(ugly[i]*primes[j], ugly[i+1]*primes[j+1]))
        if ugly[-1] == ugly[i]*primes[j]:
            i += 1
        if ugly[-1] == ugly[i+1]*primes[j+1]:
            j += 1
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()