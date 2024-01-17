class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for gap in range(n):
            for left in range(1, n - gap + 1):
                right = left + gap
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][right])
        return dp[1][n]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.maxCoins(nums))