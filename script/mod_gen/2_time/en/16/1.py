def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(len(nums)):
            if nums[j] <= i:
                dp[i] += dp[i - nums[j]]
    return dp[-1]
nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
nums = [9]
target = 3
print(combinationSum4(nums, target))
