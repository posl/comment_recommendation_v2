def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, -1, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]
    return dp[target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,22]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,23]))
print(canPartition([1,2,3,4,5,
