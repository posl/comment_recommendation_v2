def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]
nums = [1,5,11,5]
result = canPartition(nums)
print(result)

if __name__ == '__main__':
    canPartition()