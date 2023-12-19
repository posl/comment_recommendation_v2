Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

=======
Suggestion 2

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,20,30,40,50,60,70,80,90,100,110]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]))

=======
Suggestion 3

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 4

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==1: return 1
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

=======
Suggestion 5

def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
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
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 7

def lengthOfLIS(nums):
    if len(nums)==0:
        return 0
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([4,10,4,3,8,9]))
print(lengthOfLIS([0,1,0,3,2,3]))

=======
Suggestion 8

def lengthOfLIS(nums):
    n = len(nums)
    lis = [1]*n
    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j] and lis[i]<lis[j]+1:
                lis[i] = lis[j]+1
    return max(lis)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))

=======
Suggestion 9

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

=======
Suggestion 10

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10]))
