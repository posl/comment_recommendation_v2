def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums)%2!=0:
        return False
    target = sum(nums)//2
    dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0] = True
    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(nums)][target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,5,6]))
print(canPartition([1,2,5,6,10]))
print(canPartition([1,2,5,6,10,11]))
print(canPartition([1,2,5,6,10,11,12]))
print(canPartition([1,2,5,6,10,11,12,13]))
print(canPartition([1,2,5,6,10,11,12,13,15]))
print(canPartition([1,2,5,6,10,11,12,13,15,16]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19,20]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19,20,21]))
print(canPartition([1,2,5,6,10,11,12,13,15,
