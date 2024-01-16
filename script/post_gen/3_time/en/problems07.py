Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = [0] * len(primes)
        for k in range(1, n):
            ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[k] == ugly[i[j]] * primes[j]:
                    i[j] += 1
        return ugly[n-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        while len(ugly) < n:
            nextUgly = min([ugly[idx[i]] * primes[i] for i in range(len(primes))])
            ugly.append(nextUgly)
            for i in range(len(primes)):
                if ugly[idx[i]] * primes[i] == nextUgly:
                    idx[i] += 1
        return ugly[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = [0] * len(primes)
        for k in range(1, n):
            ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[k] == ugly[i[j]] * primes[j]:
                    i[j] += 1
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next_ugly = min([primes[i] * ugly[pointers[i]] for i in range(len(primes))])
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if primes[i] * ugly[pointers[i]] == next_ugly:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = 1
        index = [0] * len(primes)
        while i < n:
            min_value = min(ugly[index[j]] * primes[j] for j in range(len(primes)))
            ugly[i] = min_value
            for j in range(len(primes)):
                if ugly[index[j]] * primes[j] == min_value:
                    index[j] += 1
            i += 1
        return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = [0] * len(primes)
        for k in range(1, n):
            ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(i))])
            for j in range(len(i)):
                if ugly[k] == ugly[i[j]] * primes[j]:
                    i[j] += 1
        return ugly[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        prime_index = [0] * len(primes)
        prime = primes[0]
        for i in range(1, n):
            ugly[i] = min(primes[i] * ugly[prime_index[i]] for i in range(len(primes)))
            for j in range(len(primes)):
                if ugly[i] == primes[j] * ugly[prime_index[j]]:
                    prime_index[j] += 1
        return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next = min([ugly[pointers[i]] * primes[i] for i in range(len(primes))])
            for i in range(len(primes)):
                if ugly[pointers[i]] * primes[i] == next:
                    pointers[i] += 1
            ugly.append(next)
        return ugly[-1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        i = 1
        while i < n:
            minn = float('inf')
            for p in primes:
                minn = min(minn, ugly[0] * p)
            ugly.append(minn)
            while ugly[0] * primes[0] <= ugly[-1]:
                del ugly[0]
            i += 1
        return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
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
