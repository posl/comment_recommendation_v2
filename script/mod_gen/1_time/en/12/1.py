def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
