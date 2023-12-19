def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8]))
print(canPartition([1,2,3,4,5,6,7,8,9]))
print(canPartition([1,2,3,4,5,6,7,8,9,10]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
