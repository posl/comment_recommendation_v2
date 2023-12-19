def lengthOfLIS(nums):
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    maxLen = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                maxLen = max(maxLen, dp[i])
    return maxLen

if __name__ == '__main__':
    lengthOfLIS()