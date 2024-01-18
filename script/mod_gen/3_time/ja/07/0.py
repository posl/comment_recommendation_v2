class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ret = [1]
        #各素数のインデックス
        index = [0] * len(primes)
        #各素数の値
        val = primes.copy()
        while len(ret) < n:
            next_val = min(val)
            ret.append(next_val)
            for i in range(len(primes)):
                if next_val == val[i]:
                    index[i] += 1
                    val[i] = ret[index[i]] * primes[i]
        return ret[-1]

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))