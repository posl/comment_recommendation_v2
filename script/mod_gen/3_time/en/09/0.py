def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 == 1:
        return False
    else:
        total = total // 2
    dp = [False] * (total + 1)
    dp[0] = True
    for num in nums:
        for i in range(total, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[-1]
nums = [1, 5, 11, 5]
print(canPartition(nums))
nums = [1, 2, 3, 5]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
print(canPartition(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 16]

if __name__ == '__main__':
    canPartition()