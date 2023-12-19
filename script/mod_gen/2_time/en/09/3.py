def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums) % 2 != 0:
        return False
    target = sum(nums) // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
