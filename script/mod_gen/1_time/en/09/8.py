def canPartition(nums):
    nums.sort()
    if sum(nums) % 2 != 0:
        return False
    target = sum(nums) // 2
    dp = [[False for i in range(target + 1)] for j in range(len(nums))]
    if nums[0] <= target:
        dp[0][nums[0]] = True
    for i in range(1, len(nums)):
        for j in range(target + 1):
            if nums[i] == j:
                dp[i][j] = True
            elif nums[i] < j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(nums) - 1][target]
nums = [1,5,11,5]
result = canPartition(nums)
print(result)
nums = [1,2,3,5]
result = canPartition(nums)
print(result)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = canPartition(nums)
    print(a)