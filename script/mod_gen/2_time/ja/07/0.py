class Solution:
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

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))