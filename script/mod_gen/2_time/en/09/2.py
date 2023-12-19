def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target+1)]
    dp[0] = True
    for num in nums:
        for j in range(target, num-1, -1):
            dp[j] = dp[j] or dp[j-num]
    return dp[target]

if __name__ == '__main__':
    canPartition()