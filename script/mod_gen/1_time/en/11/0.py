class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = Solution()
    print(a.lengthOfLIS(nums))