class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum % 2 != 0:
            return False
        sum = sum // 2
        dp = [[False for _ in range(sum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, sum + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][sum]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.canPartition(nums))