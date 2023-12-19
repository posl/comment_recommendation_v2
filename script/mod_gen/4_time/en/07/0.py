def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1]
    # index of ugly number in ugly array
    index = [0] * len(primes)
    # value of ugly number in ugly array
    value = [1] * len(primes)
    # the next ugly number
    next = 1
    # loop until n
    while next < n:
        # find the minimum value of all multiples
        for i in range(len(primes)):
            value[i] = ugly[index[i]] * primes[i]
        # find the minimum value
        ugly.append(min(value))
        # update the index of ugly number
        for i in range(len(primes)):
            if ugly[-1] == value[i]:
                index[i] += 1
        # update the next ugly number
        next += 1
    # return the last ugly number
    return ugly[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()