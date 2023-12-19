Synthesizing 10/10 solutions

=======
Suggestion 1

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
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

nums = [3,4,16,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 2

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 3

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_dp = 1
    max_index = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_dp:
            max_dp = dp[i]
            max_index = i
    ans = []
    while max_index != -1:
        ans.append(nums[max_index])
        max_index = prev[max_index]
    return ans[::-1]

=======
Suggestion 4

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

nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 5

def largestDivisibleSubset(nums):
    if len(nums) == 1:
        return nums
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1]))
print(largestDivisibleSubset([1,2]))
print(largestDivisibleSubset([3,4,16,8]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64,81,128,256,512,1024]))
print(largestDivisibleSubset([1,2,4,8,9,72,16,32,64,81,128,256,512,1024,2048,4096,8192,16384,32768,65536]))

=======
Suggestion 6

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key=len)

=======
Suggestion 7

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) < 2:
        return nums
    nums.sort()
    res = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]
    return max(res, key=len)

print(largestDivisibleSubset([1,2,4,8]))

=======
Suggestion 8

def largestDivisibleSubset(nums):
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [nums[i]]
    return max(dp, key = len)

nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))

=======
Suggestion 9

def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    maxIndex = dp.index(max(dp))
    ans = []
    prev = nums[maxIndex]
    for i in range(maxIndex, -1, -1):
        if prev % nums[i] == 0 and dp[i] == dp[maxIndex]:
            ans.append(nums[i])
            prev = nums[i]
            maxIndex -= 1
    return ans[::-1]

=======
Suggestion 10

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    n = len(nums)
    dp = [0] * n
    parent = [0] * n
    mx = 0
    mx_index = -1
    for i in range(n):
        for j in range(i-1,-1,-1):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
                if dp[i] > mx:
                    mx = dp[i]
                    mx_index = i
    result = []
    for i in range(mx+1):
        result.append(nums[mx_index])
        mx_index = parent[mx_index]
    return result

print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,3,8,9,27]))
print(largestDivisibleSubset([4,8,10,240]))
print(largestDivisibleSubset([1,2,4,8,9,72]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,240]))
