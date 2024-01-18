class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = [[False for _ in range(len(stones) + 1)] for _ in range(len(stones) + 1)]
        dp[0][1] = True
        for i in range(1, len(stones)):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff < 0 or diff >= len(dp) or not dp[j][diff]:
                    continue
                dp[i][diff] = True
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 < len(dp):
                    dp[i][diff + 1] = True
        return any(dp[len(stones) - 1])

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))