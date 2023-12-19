def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(len(nums)):
            if i >= nums[j]:
                dp[i] += dp[i - nums[j]]
    return dp[target]

if __name__ == '__main__':
    combinationSum4()