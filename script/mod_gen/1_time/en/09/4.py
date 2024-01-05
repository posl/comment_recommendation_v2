def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    totalSum = sum(nums)
    if totalSum % 2 != 0:
        return False
    target = totalSum // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, -1, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]
    return dp[target]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = canPartition(nums)
    print(a)