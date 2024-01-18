Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # primesの値はすべて一意であり、昇順に並んでいる。
        # 1は素因数を持たないので、すべての素因数は配列primes = [2,3,5]に含まれる。
        # 1から始めて、primesの値で割り切れる数をリストに追加していく
        # リストの長さがnになったら終了
        ret = [1]
        i = 0
        while len(ret) < n:
            for p in primes:
                if ret[i] % p == 0:
                    ret.append(ret[i] // p)
            i += 1
        return ret[n-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        # index[i]はprimes[i]が何番目の素数かを表す
        index = [0] * len(primes)
        while len(ugly) < n:
            # すべてのprimes[i]について、ugly[index[i]] * primes[i]の最小値を求める
            # その最小値が次のugly number
            next_ugly = min(ugly[index[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next_ugly)
            # index[i]が指すugly numberが次のugly numberであれば、index[i]をインクリメントする
            for i in range(len(primes)):
                if ugly[index[i]] * primes[i] == next_ugly:
                    index[i] += 1
        return ugly[-1]

=======
Suggestion 3

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 1はsuper ugly numberなので、答えを1から探していく
        # 1から順番に、素因数がprimesにある数を掛け算していく
        # その数が答えになるかどうかを判断する
        # 答えになったら、nを1減らしていく
        # nが0になったら、答えを返す
        # 1から順番に、素因数がprimesにある数を掛け算していく
        # その数が答えになるかどうかを判断する
        # 答えになったら、nを1減らしていく
        # nが0になったら、答えを返す
        # 1から順番に、素因数がprimesにある数を掛け算していく
        # その数が答えになるかどうかを判断する
        # 答えになったら、nを1減らしていく
        # nが0になったら、答えを返す
        # 1から順番に、素因数がprimesにある数を掛け算していく
        # その数が答えになるかどうかを判断する
        # 答えになったら、nを1減らしていく
        # nが0になったら、答えを返す
        # 1から順番に、素因数がprimesにある数を掛け算していく
        # その数が答えになるかどうかを判断する
        # 答えになったら、nを1減らしていく
        # nが0になったら、答えを返す
        # 1から順番に、素因数がprimesにある数

=======
Suggestion 4

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
Suggestion 5

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        dp = [0] * len(primes)
        for _ in range(n - 1):
            ugly.append(min([ugly[dp[i]] * primes[i] for i in range(len(primes))]))
            for i in range(len(primes)):
                if ugly[-1] == ugly[dp[i]] * primes[i]:
                    dp[i] += 1
        return ugly[-1]

=======
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1
        ans = [1]
        index = [0] * len(primes)
        for i in range(1, n):
            minIndex = 0
            minValue = ans[index[0]] * primes[0]
            for j in range(1, len(primes)):
                if minValue > ans[index[j]] * primes[j]:
                    minValue = ans[index[j]] * primes[j]
                    minIndex = j
            index[minIndex] += 1
            ans.append(minValue)
        return ans[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        return 1

=======
Suggestion 8

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1]
        k = len(primes)
        idx = [0] * k
        for i in range(n - 1):
            tmp = [dp[idx[j]] * primes[j] for j in range(k)]
            dp.append(min(tmp))
            for j in range(k):
                if tmp[j] == dp[-1]:
                    idx[j] += 1
        return dp[-1]

=======
Suggestion 9

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]
        dp = [0] * len(primes)
        for _ in range(n - 1):
            next_ugly = min([ugly[dp[i]] * primes[i] for i in range(len(primes))])
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if next_ugly == ugly[dp[i]] * primes[i]:
                    dp[i] += 1
        return ugly[-1]

=======
Suggestion 10

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1]
        idx = [0] * len(primes)
        while len(dp) < n:
            candidates = [dp[idx[i]] * primes[i] for i in range(len(primes))]
            nextUgly = min(candidates)
            dp.append(nextUgly)
            for i in range(len(primes)):
                if candidates[i] == nextUgly:
                    idx[i] += 1
        return dp[-1]
