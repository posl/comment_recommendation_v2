Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = len(primes)
        primes = sorted(primes)
        index = [0] * i
        next_multiple = primes.copy()
        for j in range(1, n):
            ugly[j] = min(next_multiple)
            for k in range(i):
                if ugly[j] == next_multiple[k]:
                    index[k] += 1
                    next_multiple[k] = ugly[index[k]] * primes[k]
        return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = 1
        index = [0] * len(primes)
        while i < n:
            min_val = float('inf')
            for j in range(len(primes)):
                min_val = min(min_val, primes[j] * ugly[index[j]])
            ugly[i] = min_val
            for j in range(len(primes)):
                if min_val == primes[j] * ugly[index[j]]:
                    index[j] += 1
            i += 1
        return ugly[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next = min(ugly[pointers[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next)

            for i in range(len(primes)):
                if ugly[pointers[i]] * primes[i] == next:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)
        for i in range(1, n):
            ugly[i] = min([ugly[idx[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == ugly[idx[j]] * primes[j]:
                    idx[j] += 1
        return ugly[-1]

=======
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = 1
        while i < n:
            ugly[i] = min([ugly[j] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == ugly[j] * primes[j]:
                    j += 1
            i += 1
        return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next_ugly = min([primes[i] * ugly[pointers[i]] for i in range(len(primes))])
            for i in range(len(primes)):
                if primes[i] * ugly[pointers[i]] == next_ugly:
                    pointers[i] += 1
            ugly.append(next_ugly)
        return ugly[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        i = [0] * len(primes)
        while len(ugly) < n:
            nexts = [ugly[i[j]] * primes[j] for j in range(len(primes))]
            min_ = min(nexts)
            ugly.append(min_)
            for j in range(len(primes)):
                if min_ == nexts[j]:
                    i[j] += 1
        return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = 1
        index = [0] * len(primes)
        while i < n:
            ugly[i] = min([ugly[index[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == ugly[index[j]] * primes[j]:
                    index[j] += 1
            i += 1
        return ugly[n-1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        for _ in range(n - 1):
            next_ugly = min(ugly[pointers[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[-1] == ugly[pointers[i]] * primes[i]:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        index = [0] * len(primes)
        while len(ugly) < n:
            next_ugly = min([ugly[index[i]] * primes[i] for i in range(len(primes))])
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[-1] == ugly[index[i]] * primes[i]:
                    index[i] += 1
        return ugly[-1]
