class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        subsum = total // 2
        dp = [[False for _ in range(subsum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, subsum + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
        return dp[-1][-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))