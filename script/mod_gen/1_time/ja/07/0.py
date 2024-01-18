class Solution:
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

if __name__ == '__main__':
    n = int(input())
    primes = list(map(int, input().split()))
    a = Solution()
    print(a.nthSuperUglyNumber(n, primes))