def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
