def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for n in nums:
        for i in range(target, n - 1, -1):
            dp[i] = dp[i] or dp[i - n]
    return dp[target]
nums = [1,5,11,5]
print(canPartition(nums))
nums = [1,2,3,5]
print(canPartition(nums))
