Synthesizing 10/10 solutions

=======
Suggestion 1

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0:
                dp[i] = max(dp[i],dp[j]+1)
    maxIndex = dp.index(max(dp))
    res = [nums[maxIndex]]
    for i in range(maxIndex-1,-1,-1):
        if dp[i] == dp[maxIndex]-1 and nums[maxIndex]%nums[i] == 0:
            res.append(nums[i])
            maxIndex = i
    return res[::-1]

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,3,4,9,8]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10]))

=======
Suggestion 2

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_idx] < dp[i]:
            max_idx = i
    res = []
    while max_idx != -1:
        res.append(nums[max_idx])
        max_idx = prev[max_idx]
    return res[::-1]

=======
Suggestion 3

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

=======
Suggestion 4

def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1 for _ in range(len(nums))]
    prev = [-1 for _ in range(len(nums))]
    max_index = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[max_index] < dp[i]:
            max_index = i
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = prev[max_index]
    return res[::-1]

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))

=======
Suggestion 5

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1 for _ in range(len(nums))]
    parent = [-1 for _ in range(len(nums))]
    maxIndex = 0
    maxSize = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
        if maxSize < dp[i]:
            maxSize = dp[i]
            maxIndex = i
    res = []
    while maxIndex != -1:
        res.append(nums[maxIndex])
        maxIndex = parent[maxIndex]
    return res

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,4,6,8,10]))
print(largestDivisibleSubset([3,4,16,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,30,60]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,3,9,27,81,243,729]))
print(largestDivisibleSubset([1,2,4,8,16,32,64,128,256,512,1024,3,9,27,81,243,729,5,25,125,625]))

=======
Suggestion 6

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

nums = [1,2,3]
print(largestDivisibleSubset(nums))

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 7

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + [nums[i]], key=len)
    return max(dp, key=len)

nums = [1,2,3]
print(largestDivisibleSubset(nums))

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 8

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) <= len(dp[j]):
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len) if dp else []

=======
Suggestion 9

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([3,4,16,8]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

=======
Suggestion 10

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    max_index = dp.index(max(dp))
    res = [nums[max_index]]
    for i in range(max_index - 1, -1, -1):
        if res[-1] % nums[i] == 0 and dp[i] == dp[max_index] - 1:
            res.append(nums[i])
            max_index = i
    return res[::-1]
