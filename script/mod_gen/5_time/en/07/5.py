def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    # 1. create a list of size n to store the super ugly numbers
    # 2. create a list of size m to store the indexes of numbers to multiply by primes
    # 3. create a list of size m to store the products of numbers multiplied by primes
    # 4. create a list of size m to store the products of numbers multiplied by primes
    # 5. move the index of the smallest product to the next index
    # 6. append the smallest product to the list of super ugly numbers
    # 7. return the last element in the list of super ugly numbers
    ugly_numbers = [1]
    k = len(primes)
    indexes = [0] * k
    products = [0] * k
    for i in range(1, n):
        for j in range(k):
            products[j] = ugly_numbers[indexes[j]] * primes[j]
        ugly_numbers.append(min(products))
        for j in range(k):
            if ugly_numbers[-1] == products[j]:
                indexes[j] += 1
    return ugly_numbers[-1]

if __name__ == '__main__':
    nthSuperUglyNumber()