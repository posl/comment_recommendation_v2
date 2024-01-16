Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)
        while len(ugly) < n:
            next_ugly = min(ugly[pointers[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[pointers[i]] * primes[i] == next_ugly:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = 1
        index = [0] * len(primes)
        while i < n:
            ugly[i] = min([primes[j] * ugly[index[j]] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == primes[j] * ugly[index[j]]:
                    index[j] += 1
            i += 1
        return ugly[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)
        for i in range(1, n):
            ugly[i] = min([primes[j] * ugly[idx[j]] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == primes[j] * ugly[idx[j]]:
                    idx[j] += 1
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        prime_index = [0] * len(primes)
        prime = primes.copy()
        for i in range(1, n):
            ugly[i] = min(prime)
            for j in range(0, len(primes)):
                if ugly[i] == prime[j]:
                    prime_index[j] += 1
                    prime[j] = primes[j] * ugly[prime_index[j]]
        return ugly[n - 1]

=======
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1] * n
        idx = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min(dp[idx[j]] * primes[j] for j in range(len(primes)))
            for j in range(len(primes)):
                if dp[i] == dp[idx[j]] * primes[j]:
                    idx[j] += 1
        return dp[-1]

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        prime_index = [0] * len(primes)
        prime_value = primes.copy()
        for i in range(1, n):
            ugly[i] = min(prime_value)
            for j in range(len(primes)):
                if ugly[i] == prime_value[j]:
                    prime_index[j] += 1
                    prime_value[j] = ugly[prime_index[j]] * primes[j]
        return ugly[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        dp = [0] * len(primes)
        for i in range(1,n):
            ugly.append(min([ugly[dp[j]] * primes[j] for j in range(len(primes))]))
            for j in range(len(primes)):
                if ugly[-1] == ugly[dp[j]] * primes[j]:
                    dp[j] += 1
        return ugly[-1]

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        ugly[0] = 1
        i = [0] * len(primes)
        for k in range(1, n):
            ugly[k] = min([ugly[i[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[k] == ugly[i[j]] * primes[j]:
                    i[j] += 1
        return ugly[n - 1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [0] * n
        idx = [0] * len(primes)
        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = min([ugly[idx[j]] * primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if ugly[i] == ugly[idx[j]] * primes[j]:
                    idx[j] += 1
        return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointer = [0] * len(primes)
        for i in range(1, n):
            ugly.append(min([ugly[pointer[j]] * primes[j] for j in range(len(primes))]))
            for j in range(len(primes)):
                if ugly[i] == ugly[pointer[j]] * primes[j]:
                    pointer[j] += 1
        return ugly[-1]
