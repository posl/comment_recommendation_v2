def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    dp = [False for i in range(total + 1)]
    dp[0] = True
    for num in nums:
        for i in range(total, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[total // 2]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,22]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,23]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,
