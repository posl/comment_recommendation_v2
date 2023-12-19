def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                dp[i] += dp[i - nums[j]]
    return dp[target]
nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
