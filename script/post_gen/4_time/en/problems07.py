Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    index = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[index[j]]:
                index[j] += 1
    return ugly[-1]

primes = [2,7,13,19]
n = 12
print(nthSuperUglyNumber(n, primes))

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
    index = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float("inf")
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[index[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[index[j]]:
                index[j] += 1
    return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(n, primes):
    # Time: O(n * k) where k is len(primes)
    # Space: O(n + k)
    ugly_nums = [1]
    prime_idx = [0] * len(primes)

    for _ in range(n-1):
        candidates = [ugly_nums[prime_idx[i]] * primes[i] for i in range(len(primes))]
        min_idx = candidates.index(min(candidates))
        prime_idx[min_idx] += 1
        ugly_nums.append(candidates[min_idx])

    return ugly_nums[-1]

=======
Suggestion 5

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [0] * n
    idx = [0] * len(primes)
    ugly[0] = 1
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            while primes[j] * ugly[idx[j]] <= ugly[i]:
                idx[j] += 1
    return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(n, primes):
    ugly = [0] * n
    ugly[0] = 1
    idx = [0] * len(primes)
    for i in range(1, n):
        ugly[i] = float('inf')
        for j in range(len(primes)):
            ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        for j in range(len(primes)):
            if ugly[i] == primes[j] * ugly[idx[j]]:
                idx[j] += 1
    return ugly[-1]

print(nthSuperUglyNumber(12, [2,7,13,19]))

=======
Suggestion 7

def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
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

n = 12
primes = [2,7,13,19]
print(nthSuperUglyNumber(n, primes))
n = 1
primes = [2,3,5]
print(nthSuperUglyNumber(n, primes))

=======
Suggestion 8

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

=======
Suggestion 9

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

=======
Suggestion 10

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

print(nthSuperUglyNumber(12, [2,7,13,19]))
