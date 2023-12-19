def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    total = total // 2
    dp = [False] * (total + 1)
    dp[0] = True
    for num in nums:
        for i in range(total, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[total]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
