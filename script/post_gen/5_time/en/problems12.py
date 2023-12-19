Synthesizing 10/10 solutions

=======
Suggestion 1

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [0 for i in range(n)]
    prev = [-1 for i in range(n)]
    m = 0
    mi = -1
    for i in range(n):
        dp[i] = 1
        for j in range(i-1, -1, -1):
            if nums[i] % nums[j] == 0:
                if 1 + dp[j] > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] >= m:
            m = dp[i]
            mi = i
    ans = []
    while mi != -1:
        ans.append(nums[mi])
        mi = prev[mi]
    return ans

nums = [1,2,3]
print(largestDivisibleSubset(nums))

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 2

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_ind = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[i] > dp[max_ind]:
            max_ind = i
    ans = []
    while max_ind != -1:
        ans.append(nums[max_ind])
        max_ind = prev[max_ind]
    return ans

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

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,3,8,9,27]))

=======
Suggestion 4

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_index = 0
    for i in range(len(nums)):
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

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 5

def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    max_index = dp.index(max(dp))
    output = [nums[max_index]]
    for i in range(max_index - 1, -1, -1):
        if output[-1] % nums[i] == 0 and dp[i] == dp[max_index] - 1:
            output.append(nums[i])
            max_index = i
    return output[::-1]

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,4,8,9,72,108,540]))
print(largestDivisibleSubset([1,2,4,8,9,72,108,540,5,10,20,40,80,160,320,640]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240,480]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240,480,960]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,

=======
Suggestion 6

def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_ind = 0
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        if dp[max_ind] < dp[i]:
            max_ind = i
    result = []
    while max_ind != -1:
        result.append(nums[max_ind])
        max_ind = prev[max_ind]
    return result[::-1]


print(largestDivisibleSubset([1, 2, 3]))
print(largestDivisibleSubset([1, 2, 4, 8]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8]))
print(largestDivisibleSubset([1, 2, 4, 8, 16, 32, 64, 128]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300]))
print(largestDivisibleSubset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 300, 400]))
print(l

=======
Suggestion 7

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

print(largestDivisibleSubset([1, 2, 3]))
print(largestDivisibleSubset([1, 2, 4, 8]))

=======
Suggestion 8

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    dp = [[num] for num in nums]
    res = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
        if len(res) < len(dp[i]):
            res = dp[i]
    return res

print(largestDivisibleSubset([1,2,3]))

=======
Suggestion 9

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10]))

=======
Suggestion 10

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    if n == 1:
        return nums
    dp = [[0,[]] for i in range(n)]
    for i in range(n):
        dp[i][0] = 1
        dp[i][1].append(nums[i])
    for i in range(1,n):
        for j in range(i):
            if nums[i]%nums[j] == 0:
                if dp[i][0] < dp[j][0]+1:
                    dp[i][0] = dp[j][0]+1
                    dp[i][1] = dp[j][1][:]
                    dp[i][1].append(nums[i])
    max_len = 0
    max_index = 0
    for i in range(n):
        if dp[i][0] > max_len:
            max_len = dp[i][0]
            max_index = i
    return dp[max_index][1]
