Synthesizing 10/10 solutions

=======
Suggestion 1

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp = [1]
        idx = [0] * len(primes)
        while len(dp) < n:
            next_num = min([dp[idx[i]] * primes[i] for i in range(len(primes))])
            for i in range(len(primes)):
                if dp[idx[i]] * primes[i] == next_num:
                    idx[i] += 1
            dp.append(next_num)
        return dp[-1]

=======
Suggestion 2

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ans = [1]
        index = [0] * len(primes)
        while len(ans) < n:
            next_candidates = [ans[index[i]] * primes[i] for i in range(len(primes))]
            next_ugly = min(next_candidates)
            ans.append(next_ugly)
            for i in range(len(primes)):
                if next_ugly == next_candidates[i]:
                    index[i] += 1
        return ans[-1]

=======
Suggestion 3

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        #ダサいけど、リストに入れて、ソートして、n番目の値を返す
        ugly = [1]
        for i in range(1, n):
            ugly.append(min([ugly[j] * p for j, p in enumerate(primes)]))
            for j, p in enumerate(primes):
                if ugly[i] % p == 0:
                    primes[j] *= ugly[i]
        return ugly[-1]

=======
Suggestion 4

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 1はsuper ugly number
        ugly = [1]
        # primesの数だけpointerを用意
        pointers = [0] * len(primes)
        # 1からnまで回す
        for _ in range(1, n):
            # それぞれのpointerを回して最小値を求める
            candidates = [ugly[pointers[i]] * primes[i] for i in range(len(primes))]
            # 最小値をuglyに追加
            ugly.append(min(candidates))
            # 最小値と同じ値であればpointerを進める
            for i in range(len(primes)):
                if candidates[i] == ugly[-1]:
                    pointers[i] += 1
        return ugly[-1]

=======
Suggestion 5

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
Suggestion 6

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1
        ans = [1]
        index = [0] * len(primes)
        for i in range(n-1):
            min_num = min([ans[index[j]] * primes[j] for j in range(len(primes))])
            ans.append(min_num)
            for j in range(len(primes)):
                if ans[-1] == ans[index[j]] * primes[j]:
                    index[j] += 1
        return ans[-1]

=======
Suggestion 7

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        if n == 1:
            return 1
        ugly = [1]
        k = len(primes)
        i = [0]*k
        for j in range(1,n):
            ugly.append(min([ugly[i[l]]*primes[l] for l in range(k)]))
            for l in range(k):
                if ugly[-1] == ugly[i[l]]*primes[l]:
                    i[l] += 1
        return ugly[-1]

=======
Suggestion 8

    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 解答1
        # 1はどの素数でも割り切れるので、1を初期値としておく
        ugly = [1]
        # primesの数だけ、indexを初期値としておく
        index = [0] * len(primes)
        # n回繰り返す
        for _ in range(n):
            # primesの数だけ、素数を掛けた値を生成する
            # その中から最小値を取得する
            ugly.append(min([ugly[index[i]] * primes[i] for i in range(len(primes))]))
            # 最小値と等しい値を持つ素数のindexを増やす
            for i in range(len(primes)):
                if ugly[-1] == ugly[index[i]] * primes[i]:
                    index[i] += 1
        return ugly[-2]
        # 解答2
        # 1はどの素数でも割り切れるので、1を初期値としておく
        ugly = [1]
        # primesの数だけ、indexを初期値としておく
        index = [0] * len(primes)
        # n回繰り返す
        for _ in range(n):
            # primesの数だけ、素数を掛けた値を生成する
            # その中から最小値を取得する
            temp = [ugly[index[i]] * primes[i] for i in range(len(primes))]
            # 最小値と等しい値を持つ素数のindexを増やす
            for i in range(len(primes)):
                if ugly[-1] == temp[i]:
                    index[i] += 1
            ugly.append(min(temp))
        return ugly[-2]
        # 解答3
        # 1はどの素数でも割り切れるので、1を初期値としておく
        ugly = [1]
        # primesの数だけ、indexを初期値としておく
        index = [0] *

=======
Suggestion 9

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32
        # 1, 2, 4, 8, 16, 32
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23
        # 1, 2, 3, 5, 7, 11, 13, 17, 19, 23

        # 1
        # 1, 2, 3, 5,

=======
Suggestion 10

def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 素因数を保持する配列
        factors = [0] * len(primes)

        # ugly numberを保持する配列
        ugly = [1]

        # n個の ugly number を生成する
        for _ in range(1, n):
            # 素因数をそれぞれ掛け合わせた値を生成する
            # その中から最小値を選ぶ
            # ugly number を生成する
            ugly_numbers = [ugly[factors[i]] * primes[i] for i in range(len(primes))]
            min_ugly = min(ugly_numbers)
            ugly.append(min_ugly)

            # 最小値を選んだ素因数のインデックスを進める
            for i in range(len(primes)):
                if ugly_numbers[i] == min_ugly:
                    factors[i] += 1

        return ugly[-1]
