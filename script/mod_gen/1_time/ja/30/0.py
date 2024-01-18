class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = [[False for _ in range(len(stones))] for _ in range(len(stones))]
        dp[0][0] = True
        for i in range(1, len(stones)):
            for j in range(i):
                k = stones[i] - stones[j]
                if k < 0 or k >= len(stones) or not dp[j][k]:
                    continue
                dp[i][k] = True
                if k - 1 >= 0:
                    dp[i][k - 1] = True
                if k + 1 < len(stones):
                    dp[i][k + 1] = True
        return any(dp[-1])

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))