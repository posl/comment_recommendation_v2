Synthesizing 10/10 solutions (Duplicates hidden)

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
        return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly_numbers = [1]
        ugly_numbers_set = {1}
        prime_index = [0] * len(primes)
        for i in range(n - 1):
            min_value = min([primes[j] * ugly_numbers[prime_index[j]] for j in range(len(primes))])
            ugly_numbers.append(min_value)
            for j in range(len(primes)):
                if primes[j] * ugly_numbers[prime_index[j]] == min_value:
                    prime_index[j] += 1
        return ugly_numbers[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1] * n
        pointers = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min([dp[pointers[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if dp[i] == dp[pointers[j]] * primes[j]:
                    pointers[j] += 1
        return dp[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        def gen(prime):
            for u in ugly:
                yield u*prime
        merged = heapq.merge(*map(gen, primes))
        while len(ugly) < n:
            u = next(merged)
            if u != ugly[-1]:
                ugly.append(u)
        return ugly[-1]

=======
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        index = [0] * len(primes)
        for _ in range(n - 1):
            uglyNumbers = [ugly[index[i]] * primes[i] for i in range(len(primes))]
            uglyNext = min(uglyNumbers)
            ugly.append(uglyNext)
            for i in range(len(primes)):
                if uglyNext == uglyNumbers[i]:
                    index[i] += 1
        return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            candidates = [primes[i] * ugly[pointers[i]] for i in range(len(primes))]
            next_ugly = min(candidates)
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if candidates[i] == next_ugly:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
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
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        def gen(prime):
            for u in ugly:
                yield u * prime
        merged = heapq.merge(*map(gen, primes))
        while len(ugly) < n:
            uglies = itertools.takewhile(lambda x: x > ugly[-1], merged)
            ugly.append(next(uglies))
        return ugly[-1]
