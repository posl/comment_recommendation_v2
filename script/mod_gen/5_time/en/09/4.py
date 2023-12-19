def canPartition(nums):
    sum = 0
    for num in nums:
        sum += num
    if sum % 2 != 0:
        return False
    else:
        target = sum // 2
        dp = [False for i in range(target + 1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
