Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        i = 0
        while len(ugly) < n:
            ugly.append(min([ugly[j] * primes[i] for j in range(len(ugly))]))
            i = ugly.index(ugly[-1] / primes[i])
        return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        k = len(primes)
        idx = [0] * k
        vals = [0] * k
        for i in range(1, n):
            for j in range(k):
                vals[j] = ugly[idx[j]] * primes[j]
            ugly.append(min(vals))
            for j in range(k):
                if ugly[-1] == vals[j]:
                    idx[j] += 1
        return ugly[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        idx = [0] * len(primes)
        val = [1] * len(primes)
        next = 1
        for i in range(n):
            ugly[i] = next
            next = float('inf')
            for j in range(len(primes)):
                if val[j] == ugly[i]:
                    val[j] = ugly[idx[j]] * primes[j]
                    idx[j] += 1
                next = min(next, val[j])
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        dp = [0] * len(primes)
        for _ in range(n - 1):
            next_ugly = min([ugly[dp[i]] * primes[i] for i in range(len(primes))])
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[dp[i]] * primes[i] == next_ugly:
                    dp[i] += 1
        return ugly[-1]

=======
Suggestion 5

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

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1]
        idx = [0] * len(primes)
        for _ in range(n-1):
            dp.append(min(dp[idx[i]] * primes[i] for i in range(len(idx))))
            for i in range(len(idx)):
                if dp[-1] == dp[idx[i]] * primes[i]:
                    idx[i] += 1
        return dp[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        k = len(primes)
        idx = [0] * k
        for i in range(1, n):
            ugly[i] = min([ugly[idx[j]] * primes[j] for j in range(k)])
            for j in range(k):
                if ugly[i] == ugly[idx[j]] * primes[j]:
                    idx[j] += 1
        return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        while len(ugly) < n:
            nexts = [ugly[idx[i]] * primes[i] for i in range(len(primes))]
            min_next = min(nexts)
            ugly.append(min_next)
            for i in range(len(primes)):
                if nexts[i] == min_next:
                    idx[i] += 1
        return ugly[-1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        for i in range(1, n):
            ugly.append(min([ugly[pointers[j]] * primes[j] for j in range(len(primes))]))
            for j in range(len(primes)):
                if ugly[-1] == ugly[pointers[j]] * primes[j]:
                    pointers[j] += 1
        return ugly[-1]
