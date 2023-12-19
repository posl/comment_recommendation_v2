Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def is_valid(nums, m, max_sum):
        splits, curr_sum = 1, 0
        for n in nums:
            if curr_sum + n > max_sum:
                splits += 1
                curr_sum = n
            else:
                curr_sum += n
        return splits <= m
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, m, mid):
            right = mid
        else:
            left = mid + 1
    return left

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
nums = [1,2,3,4,5]
k = 2
print(splitArray(nums, k))

=======
Suggestion 2

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    
    def check(mid):
        total = 0
        count = 1
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > m:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 3

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        cuts, curr_sum = 1, 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cuts += 1
                curr_sum = num
        return cuts <= k
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 4

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def is_valid(nums, m, mid):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > m:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if is_valid(nums, m, mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 5

def splitArray(nums, k):
    start = max(nums)
    end = sum(nums)
    while start < end:
        mid = (start + end) // 2
        if check(nums, mid, k):
            end = mid
        else:
            start = mid + 1
    return start

=======
Suggestion 6

def splitArray(nums, k):
    
    def isPossible(mid):
        count = 1
        subarraySum = 0
        for num in nums:
            subarraySum += num
            if subarraySum > mid:
                count += 1
                subarraySum = num
        return count <= k
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(mid):
            right = mid
        else:
            left = mid + 1
    return left

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))
nums = [1,2,3,4,5]
k = 2
print(splitArray(nums, k))
nums = [1,4,4]
k = 3
print(splitArray(nums, k))

=======
Suggestion 7

def splitArray(nums, k):
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isValid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 8

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    n = len(nums)
    dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0
    sub = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        sub[i] = sub[i-1] + nums[i-1]
    for i in range(1, m+1):
        for j in range(i, n+1):
            for k in range(i-1, j):
                dp[i][j] = min(dp[i][j], max(dp[i-1][k], sub[j] - sub[k]))
    return dp[m][n]

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,2,3,4,5], 3))
print(splitArray([1,2147483647], 2))
print(splitArray([1,2,3,4,5], 1))
print(splitArray([1,2,3,4,5], 5))
print("The values above should be 18, 9, 4, 6, 2147483647, 15, 5, and 5.")

=======
Suggestion 9

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # O(n^2)
    # dp[i][j] is the minimum largest sum of splitting nums[0] ~ nums[i] into j parts
    # dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1]))) for k in range(i)
    # ans = dp[-1][-1]
    # dp = [[float('inf')] * (m+1) for _ in range(len(nums))]
    # dp[0][1] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i][1] = dp[i-1][1] + nums[i]
    # for i in range(1, len(nums)):
    #     for j in range(2, min(i+2, m+1)):
    #         for k in range(i):
    #             dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1])))
    # return dp[-1][-1]

    # O(nlog(sum))
    # dp[i][j] is the minimum largest sum of splitting nums[0] ~ nums[i] into j parts
    # dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1]))) for k in range(i)
    # ans = dp[-1][-1]
    # dp = [[float('inf')] * (m+1) for _ in range(len(nums))]
    # dp[0][1] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i][1] = dp[i-1][1] + nums[i]
    # for i in range(1, len(nums)):
    #     for j in range(2, min(i+2, m+1)):
    #         l, r = 0, i
    #         while l < r:
    #             mid = (l+r) // 2
    #             if dp[mid][j-1] > sum(nums[mid+1:i+1]):
    #                 r = mid
    #

=======
Suggestion 10

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l + r) // 2
        if valid(mid, nums, k):
            r = mid
        else:
            l = mid + 1
    return l
