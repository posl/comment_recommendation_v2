class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxCoins(nums))