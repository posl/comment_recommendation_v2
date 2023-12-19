def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    target = total//2
    if total%2 != 0:
        return False
    else:
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[-1]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,1,1,1,1,1,1,1,1,1]))
print(canPartition([1,1,1,1,1,1,1,1,1,10]))
print(canPartition([1,1,1,1,1,1,1,1,1,11]))
print(canPartition([1,1,1,1,1,1,1,1,1,12]))
print(canPartition([1,1,1,1,1,1,1,1,1,13]))
print(canPartition([1,1,1,1,1,1,1,1,1,14]))
print(canPartition([1,1,1,1,1,1,1,1,1,15]))
print(canPartition([1,1,1,1,1,1,1,1,1,16]))
print(canPartition([1,1,1,1,1,1,1,1,1,17]))
print(canPartition([1,1,1,1,1,1,1,1,1,18]))
print(canPartition([1,1,1,1,1,1,1,1,1,19]))
print(canPartition([1,1,1,1,1,1,1,1,1,20]))
print(canPartition([1,1,1,1,1,1,1,1,1,21]))
print(canPartition([1,1,1,1,1,1,1,1,1,22]))
print(canPartition([1,1,1,1,1,
