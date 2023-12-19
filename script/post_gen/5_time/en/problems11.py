Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 2

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 1
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 3

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # DP solution
    if not nums:
        return 0
    dp = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 4

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

=======
Suggestion 5

def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 6

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0]))
print(lengthOfLIS([])))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([1,

=======
Suggestion 7

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if(nums[i] > nums[j]):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 8

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8]))
print(length

=======
Suggestion 9

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2: return len(nums)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [1,3,6,7,9,4,10,5,6]
print(lengthOfLIS(nums))

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(lengthOfLIS(nums))

=======
Suggestion 10

def lengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
