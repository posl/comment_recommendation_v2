def lengthOfLIS(nums):
    if len(nums)==0:
        return 0
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([0,1,0,3,2,3]))
