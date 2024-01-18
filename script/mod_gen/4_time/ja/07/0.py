class Solution:
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

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))