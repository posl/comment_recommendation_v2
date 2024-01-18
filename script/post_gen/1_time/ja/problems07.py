Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        k = len(primes)
        p = [0] * k
        for i in range(1, n):
            dp[i] = min(dp[p[j]] * primes[j] for j in range(k))
            for j in range(k):
                if dp[i] == dp[p[j]] * primes[j]:
                    p[j] += 1
        return dp[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        k = len(primes)
        dp = [0] * n
        dp[0] = 1
        index = [0] * k
        for i in range(1, n):
            dp[i] = min([dp[index[j]] * primes[j] for j in range(k)])
            for j in range(k):
                if dp[i] == dp[index[j]] * primes[j]:
                    index[j] += 1
        return dp[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        def getlcm(a, b):
            return a * b // math.gcd(a, b)
        def getugly(prime, i):
            if i == 0:
                return 1
            return ugly[i] * prime
        def getmin(primes):
            min = math.inf
            for i in range(len(primes)):
                if primes[i] < min:
                    min = primes[i]
            return min
        primes.sort()
        while len(ugly) < n:
            min = math.inf
            for i in range(len(primes)):
                min = min if min < getugly(primes[i], len(ugly) - 1) else getugly(primes[i], len(ugly) - 1)
            ugly.append(min)
            for i in range(len(primes)):
                if min == getugly(primes[i], len(ugly) - 1):
                    primes[i] *= primes[i]
        #print(ugly)
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        pass

=======
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        pointers = [0] * len(primes)

        for _ in range(n - 1):
            next_ugly = min([ugly[pointers[i]] * primes[i] for i in range(len(primes))])
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if ugly[-1] == ugly[pointers[i]] * primes[i]:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 6

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
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # O(n log n)
        import heapq
        heap = [1]
        seen = set()
        for _ in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                new_ugly = ugly * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return ugly

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 1はsuper ugly number
        ugly = [1]
        # primesの数だけpointerを用意
        pointers = [0] * len(primes)
        # n-1回ループする
        while len(ugly) < n:
            # primesの数だけpointerを用意
            candidates = [ugly[pointers[i]] * primes[i] for i in range(len(primes))]
            # candidatesの中で最小の値をuglyに追加
            ugly.append(min(candidates))
            # candidatesの中で最小の値を持つpointerを+1する
            for i in range(len(primes)):
                if candidates[i] == ugly[-1]:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # ugly number は 1 から始まる
        ugly = [1]
        # primes の要素数分の index を持つ配列
        index = [0] * len(primes)
        # n 番目の ugly number を求める
        for _ in range(n - 1):
            # primes の要素を掛けて、最小値を求める
            ugly.append(min([ugly[index[i]] * primes[i] for i in range(len(primes))]))
            # 最小値の index に +1 する
            for i in range(len(primes)):
                if ugly[-1] == ugly[index[i]] * primes[i]:
                    index[i] += 1
        return ugly[-1]

=======
Suggestion 10

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 計算量 O(NlogN)
        # 素数の個数をKとして、NlogN
        # 素数の個数が少ない場合は、N*K
        # 素数の個数が多い場合は、NlogN
        # N: n
        # K: len(primes)
        # 1 <= n <= 105
        # 1 <= primes.length <= 100
        # 2 <= primes[i] <= 1000
        # primes[i]は素数であることが保証される。
        # primesの値はすべて一意であり、昇順に並んでいる。
        # 1 <= primes[i] <= 1000
        # primes[i]は素数であることが保証される。
        # primesの値はすべて一意であり、昇順に並んでいる。
        # 素数の個数が少ない場合は、N*K
        # 素数の個数が多い場合は、NlogN
        # N: n
        # K: len(primes)
        # 1 <= n <= 105
        # 1 <= primes.length <= 100
        # 2 <= primes[i] <= 1000
        # primes[i]は素数であることが保証される。
        # primesの値はすべて一意であり、昇順に並んでいる。
        # 素数の個数が少ない場合は、N*K
        # 素数の個数が多い場合は、NlogN
        # N: n
        # K: len(primes)
        # 1 <= n <= 105
        # 1 <= primes.length <= 100
        # 2 <= primes[i] <= 1000
        # primes[i]は素数であることが保証される。
        # primesの値はすべて一意であり、昇順に
