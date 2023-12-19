Synthesizing 10/10 solutions

=======
Suggestion 1

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

=======
Suggestion 2

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums)%2!=0:
        return False
    else:
        target = sum(nums)/2
        dp = [False for i in range(int(target)+1)]
        dp[0] = True
        for num in nums:
            for i in range(len(dp)-1,-1,-1):
                if dp[i]:
                    dp[i+num] = True
            if dp[-1]:
                return True
        return False

=======
Suggestion 3

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

=======
Suggestion 4

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
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
Suggestion 5

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

=======
Suggestion 6

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    dp = [False for i in range(total + 1)]
    dp[0] = True
    for num in nums:
        for i in range(total, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[total // 2]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,22]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,23]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,

=======
Suggestion 7

def canPartition(nums):
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

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

=======
Suggestion 8

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    nums.reverse()
    sum_of_nums = sum(nums)
    if sum_of_nums % 2 != 0:
        return False
    half_sum = sum_of_nums // 2
    if half_sum in nums:
        return True
    for i in range(0, len(nums)):
        sum_of_subset = nums[i]
        if sum_of_subset > half_sum:
            continue
        for j in range(i+1, len(nums)):
            sum_of_subset += nums[j]
            if sum_of_subset > half_sum:
                break
            elif sum_of_subset == half_sum:
                return True
    return False

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21]))
print

=======
Suggestion 9

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

=======
Suggestion 10

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

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,3,4,5,6,7]))
