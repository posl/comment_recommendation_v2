def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    # Initialize the list of super ugly numbers with the first prime number
    super_ugly = [1]
    # Initialize the list of prime numbers with the given list of primes
    prime_numbers = primes
    # Initialize the list of indexes, each index corresponding to the index of the super ugly number
    # that is being multiplied with the corresponding prime number
    indexes = [0] * len(prime_numbers)
    # Initialize the list of products, each product corresponding to the product of the super ugly number
    # that is being multiplied with the corresponding prime number
    products = [1] * len(prime_numbers)
    # Initialize the list of next super ugly numbers, each next super ugly number corresponding to the
    # next super ugly number that is being multiplied with the corresponding prime number
    next_super_ugly = [1] * len(prime_numbers)
    # While the length of the list of super ugly numbers is less than n
    while len(super_ugly) < n:
        # For each prime number in the list of prime numbers
        for i in range(len(prime_numbers)):
            # The product of the next super ugly number and the prime number is equal to the product
            # of the super ugly number that is being multiplied with the corresponding prime number
            # multiplied by the prime number
            next_super_ugly[i] = super_ugly[indexes[i]] * prime_numbers[i]
        # The next super ugly number is equal to the minimum of the list of next super ugly numbers
        next_ugly = min(next_super_ugly)
        # For each prime number in the list of prime numbers
        for i in range(len(prime_numbers)):
            # If the next super ugly number is equal to the next super ugly number multiplied by the
            # corresponding prime number
            if next_ugly == next_super_ugly[i]:
                # The super ugly number that is being multiplied with the corresponding prime number
                # is equal to the next super ugly number
                indexes[i] += 1
        # The super ugly number is equal to the next super ugly number
        super_ugly.append(next_ugly)
    # Return the n

if __name__ == '__main__':
    nthSuperUglyNumber()