Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

=======
Suggestion 2

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if primes[j] * ugly[idx[j]] == ugly[i]:
                idx[j] += 1
    return ugly[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(100000, [2,3,5]))
print(nthSuperUglyNumber(100000, [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]))

=======
Suggestion 3

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    for k in range(1, n):
        ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[k] == ugly[i[j]] * primes[j]:
                i[j] += 1
    return ugly[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))
print(nthSuperUglyNumber(1, [2,3,5]))
print(nthSuperUglyNumber(15, [2,3,5]))
print(nthSuperUglyNumber(20, [2,3,5]))
print(nthSuperUglyNumber(25, [2,3,5]))
print(nthSuperUglyNumber(30, [2,3,5]))
print(nthSuperUglyNumber(35, [2,3,5]))
print(nthSuperUglyNumber(40, [2,3,5]))
print(nthSuperUglyNumber(45, [2,3,5]))
print(nthSuperUglyNumber(50, [2,3,5]))
print(nthSuperUglyNumber(55, [2,3,5]))
print(nthSuperUglyNumber(60, [2,3,5]))
print(nthSuperUglyNumber(65, [2,3,5]))
print(nthSuperUglyNumber(70, [2,3,5]))
print(nthSuperUglyNumber(75, [2,3,5]))
print(nthSuperUglyNumber(80, [2,3,5]))
print(nthSuperUglyNumber(85, [2,3,5]))
print(nthSuperUglyNumber(90, [2,3,5]))
print(nthSuperUglyNumber(95, [2,3,5]))
print(nthSuperUglyNumber(100, [2,3,5]))
print(nthSuperUglyNumber(105, [2,3,5]))
print(nthSuperUgly

=======
Suggestion 4

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp = [1]
    idx = [0] * len(primes)
    while len(dp) < n:
        temp = []
        for i in range(len(primes)):
            temp.append(dp[idx[i]] * primes[i])
        m = min(temp)
        dp.append(m)
        for i in range(len(primes)):
            if m == temp[i]:
                idx[i] += 1
    return dp[-1]

=======
Suggestion 5

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

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
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

=======
Suggestion 9

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    i = [0] * len(primes)
    for k in range(1, n):
        ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
        for j in range(len(primes)):
            if ugly[k] == ugly[i[j]] * primes[j]:
                i[j] += 1
    return ugly[-1]
