def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))
nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))
