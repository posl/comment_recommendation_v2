def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if i-n >= 0:
                dp[i] += dp[i-n]
    return dp[target]
print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
