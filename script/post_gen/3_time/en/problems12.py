Synthesizing 10/10 solutions

=======
Suggestion 1

def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1]*n
    parent = [-1]*n
    max_ind = 0
    max_val = 0
    for i in range(n):
        for j in range(i):
            if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                parent[i] = j
        if dp[i]>max_val:
            max_val = dp[i]
            max_ind = i
    res = []
    while max_ind!=-1:
        res.append(nums[max_ind])
        max_ind = parent[max_ind]
    return res

nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [2,3,8,9,27]
print(largestDivisibleSubset(nums))
nums = [5,9,18,54,108,540,90,180,360,720]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8,9,72]
print(largestDivisibleSubset(nums))
nums = [1,2,3]
print(largestDivisible

=======
Suggestion 2

def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    max_len = 0
    max_index = -1
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = parent[max_index]
    return res[::-1]

nums = [1,2,3]
print(largestDivisibleSubset(nums))

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 3

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
Suggestion 4

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 5

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
Suggestion 6

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[i] for i in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
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
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_idx = 0
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_idx] < dp[i]:
            max_idx = i
    ans = []
    while max_idx != -1:
        ans.append(nums[max_idx])
        max_idx = prev[max_idx]
    return ans[::-1]

=======
Suggestion 8

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([3,4,16,8]))

=======
Suggestion 9

def largestDivisibleSubset(nums):
    n = len(nums)
    nums.sort()
    dp = [1] * n
    prev = [-1] * n
    max_val = 0
    max_idx = -1
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_val:
            max_val = dp[i]
            max_idx = i
    ans = []
    while max_idx != -1:
        ans.append(nums[max_idx])
        max_idx = prev[max_idx]
    return ans[::-1]

print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960,1080]))
print(largestDivisibleSubset([1,2,4,8,9,72,100,128,240,360,480,720,840,960,1080,1200]))
print(largestDivisibleSubset([1,2,4,8,9,72,100

=======
Suggestion 10

def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1 for i in range(n)]
    prev = [-1 for i in range(n)]
    max_ind = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[max_ind] < dp[i]:
            max_ind = i
    ans = []
    while max_ind != -1:
        ans.append(nums[max_ind])
        max_ind = prev[max_ind]
    return ans[::-1]

nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))
