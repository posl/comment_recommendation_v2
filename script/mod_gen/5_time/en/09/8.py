def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[-1]
nums = [1,5,11,5]
print(canPartition(nums))
nums = [1,2,3,5]
print(canPartition(nums))
