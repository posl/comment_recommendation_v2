def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1 for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
