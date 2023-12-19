Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) < 2:
        return False

    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]

=======
Suggestion 3

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total%2 == 1:
        return False
    target = total/2
    nums.sort()
    if nums[-1] > target:
        return False
    if nums[-1] == target:
        return True
    return canPartitionHelper(nums[:-1], target-nums[-1])

=======
Suggestion 4

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] |= dp[i - num]
    return dp[target]

nums = [1,5,11,5]
print(canPartition(nums))
nums = [1,2,3,5]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,

=======
Suggestion 5

def canPartition(nums):
    if sum(nums)%2 != 0:
        return False
    else:
        return True

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

=======
Suggestion 6

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

=======
Suggestion 7

def canPartition(nums):
    # Write your code here
    pass

=======
Suggestion 8

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = sum(nums)
    if s % 2 != 0:
        return False
    target = s // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

=======
Suggestion 9

def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))

=======
Suggestion 10

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
