Synthesizing 10/10 solutions

=======
Suggestion 1

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, -1, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,22]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,23]))
print(canPartition([1,2,3,4,5,

=======
Suggestion 2

def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    else:
        target = sum(nums) // 2
        dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,

=======
Suggestion 3

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) / 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[-1]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,5,6]))
print(canPartition([1,2,5,6,7]))
print(canPartition([1,2,5,6,7,8]))
print(canPartition([1,2,5,6,7,8,9]))
print(canPartition([1,2,5,6,7,8,9,10]))
print(canPartition([1,2,5,6,7,8,9,10,11]))
print(canPartition([1,2,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14,15,16]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(canPartition([1,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))
print(canPartition([1,

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
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8]))
print(canPartition([1,2,3,4,5,6,7,8,9]))
print(canPartition([1,2,3,4,5,6,7,8,9,10]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

=======
Suggestion 5

def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

=======
Suggestion 6

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    return dfs(nums, target, 0, {})

=======
Suggestion 7

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

=======
Suggestion 8

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    target = total//2
    if total%2 != 0:
        return False
    else:
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[-1]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,1,1,1,1,1,1,1,1,1]))
print(canPartition([1,1,1,1,1,1,1,1,1,10]))
print(canPartition([1,1,1,1,1,1,1,1,1,11]))
print(canPartition([1,1,1,1,1,1,1,1,1,12]))
print(canPartition([1,1,1,1,1,1,1,1,1,13]))
print(canPartition([1,1,1,1,1,1,1,1,1,14]))
print(canPartition([1,1,1,1,1,1,1,1,1,15]))
print(canPartition([1,1,1,1,1,1,1,1,1,16]))
print(canPartition([1,1,1,1,1,1,1,1,1,17]))
print(canPartition([1,1,1,1,1,1,1,1,1,18]))
print(canPartition([1,1,1,1,1,1,1,1,1,19]))
print(canPartition([1,1,1,1,1,1,1,1,1,20]))
print(canPartition([1,1,1,1,1,1,1,1,1,21]))
print(canPartition([1,1,1,1,1,1,1,1,1,22]))
print(canPartition([1,1,1,1,1,

=======
Suggestion 9

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

=======
Suggestion 10

def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] |= dp[i - num]
    return bool(dp[target])

nums = [1,5,11,5]
print(canPartition(nums))
nums = [1,2,3,5]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(canPartition(nums
