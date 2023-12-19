def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    # 1. Initialize the array of ugly numbers
    ugly = [0] * n
    ugly[0] = 1
    # 2. Initialize the array of prime indices
    prime_index = [0] * len(primes)
    # 3. Initialize the array of next multiples
    next_multiple = primes[:]
    # 4. Initialize the next ugly number to 1
    next_ugly = 1
    # 5. Loop until the n^th ugly number
    for i in range(1, n):
        # 6. Get the next ugly number
        next_ugly = min(next_multiple)
        # 7. Add the next ugly number to the array
        ugly[i] = next_ugly
        # 8. Loop through the primes
        for j in range(len(primes)):
            # 9. If the next ugly number is equal to the next multiple of the prime
            if next_ugly == next_multiple[j]:
                # 10. Increment the prime index
                prime_index[j] += 1
                # 11. Get the next multiple of the prime
                next_multiple[j] = ugly[prime_index[j]] * primes[j]
    # 12. Return the n^th ugly number
    return next_ugly

if __name__ == '__main__':
    nthSuperUglyNumber()