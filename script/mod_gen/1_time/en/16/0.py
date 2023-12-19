def combinationSum4(nums, target):
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i-num]
    return dp[target]
nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
