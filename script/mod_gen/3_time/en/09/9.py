def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total%2 != 0:
        return False
    target = total//2
    dp = [[False for j in range(target+1)] for i in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0] = True
    for i in range(1, len(nums)+1):
        for j in range(1, target+1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[-1][-1]

if __name__ == '__main__':
    canPartition()