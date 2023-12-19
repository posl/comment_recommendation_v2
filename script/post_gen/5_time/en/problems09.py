Synthesizing 10/10 solutions

=======
Suggestion 1

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if sum(nums)%2 != 0:
        return False
    target = sum(nums)//2
    dp = [False]*(target+1)
    dp[0] = True
    for num in nums:
        for i in range(target, num-1, -1):
            dp[i] = dp[i] or dp[i-num]
    return dp[target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

=======
Suggestion 2

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

nums = [1,2,5]
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

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(canPartition(nums))

nums = [1,2,3,4,5,6,7,8,

=======
Suggestion 3

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    print(nums)
    sum = 0
    for num in nums:
        sum += num
    print(sum)
    if sum % 2 != 0:
        return False
    else:
        target = sum // 2
        print(target)
        return helper(nums, 0, target)

=======
Suggestion 4

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

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]


nums = [1,2,3,5]
print(canPartition(nums))

=======
Suggestion 5

def canPartition(nums):
    sum = 0
    for num in nums:
        sum += num
    if sum % 2 != 0:
        return False
    else:
        target = sum // 2
        dp = [False for i in range(target + 1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
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
    if sum(nums)%2!=0:
        return False
    target = sum(nums)//2
    dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
    for i in range(len(nums)+1):
        dp[i][0] = True
    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(nums)][target]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,5]))
print(canPartition([1,2,5,6]))
print(canPartition([1,2,5,6,10]))
print(canPartition([1,2,5,6,10,11]))
print(canPartition([1,2,5,6,10,11,12]))
print(canPartition([1,2,5,6,10,11,12,13]))
print(canPartition([1,2,5,6,10,11,12,13,15]))
print(canPartition([1,2,5,6,10,11,12,13,15,16]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19,20]))
print(canPartition([1,2,5,6,10,11,12,13,15,16,17,18,19,20,21]))
print(canPartition([1,2,5,6,10,11,12,13,15,

=======
Suggestion 7

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    else:
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

print(canPartition([1,5,11,5]))

=======
Suggestion 8

def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

print(canPartition([1,5,11,5])) # True
print(canPartition([1,2,3,5])) # False
print(canPartition([1,2,3,4,5,6,7])) # True
print(canPartition([1,2,3,4,5,6,8])) # False
print(canPartition([1,2,3,4,5,6,9])) # False
print(canPartition([1,2,3,4,5,6,10])) # True
print(canPartition([1,2,3,4,5,6,11])) # False
print(canPartition([1,2,3,4,5,6,12])) # True
print(canPartition([1,2,3,4,5,6,13])) # False
print(canPartition([1,2,3,4,5,6,14])) # True
print(canPartition([1,2,3,4,5,6,15])) # False
print(canPartition([1,2,3,4,5,6,16])) # True
print(canPartition([1,2,3,4,5,6,17])) # False
print(canPartition([1,2,3,4,5,6,18])) # True
print(canPartition([1,2,3,4,5,6,19])) # False
print(canPartition([1,2,3,4,5,6,20])) # True
print(canPartition([1,2,3,4,5,6,21])) # False
print(canPartition([1,2,3,4,5,6,22])) # True
print(canPartition([1,2,3,4,5,6,23])) # False
print

=======
Suggestion 9

def canPartition(nums):
    total = sum(nums)
    if total % 2 == 1:
        return False
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[-1]

nums = [1,5,11,5]
print(canPartition(nums))

nums = [1,2,3,5]
print(canPartition(nums))

=======
Suggestion 10

def canPartition(nums):
    if sum(nums) % 2 == 1:
        return False
    else:
        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][target]
