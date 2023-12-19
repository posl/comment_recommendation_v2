Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isValid(nums, mid, k):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                count += 1
                currSum = num
        return count <= k
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isValid(nums, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))

=======
Suggestion 2

def splitArray(nums, k):
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(nums, k, mid):
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
    def valid(mid):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > k:
                    return False
        return True
        
    l, r = max(nums), sum(nums)
    while l < r:
        mid = l + (r-l)//2
        if valid(mid):
            r = mid
        else:
            l = mid + 1
    return l

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))

=======
Suggestion 4

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def valid(mid):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                count += 1
                if count > k:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if valid(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))

=======
Suggestion 5

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = (l + r) // 2
        if check(nums, mid, k):
            r = mid
        else:
            l = mid + 1
    return l

=======
Suggestion 6

def splitArray(nums, k):
    def canSplit(nums, k, x):
        count = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr > x:
                curr = nums[i]
                count += 1
                if count >= k:
                    return False
        return True
    
    l, r = max(nums), sum(nums)
    while l < r:
        mid = l + (r - l) // 2
        if canSplit(nums, k, mid):
            r = mid
        else:
            l = mid + 1
    return l

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))

=======
Suggestion 7

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    pass

=======
Suggestion 8

def splitArray(nums, k):
    n = len(nums)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    sub = [0]
    for num in nums:
        sub.append(sub[-1] + num)
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for p in range(i):
                dp[i][j] = min(dp[i][j], max(dp[p][j - 1], sub[i] - sub[p]))
    return dp[n][k]

nums = [7,2,5,10,8]
k = 2
result = splitArray(nums, k)
print(result)

=======
Suggestion 9

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # The idea is to use binary search to search the answer.
    # The answer is between max(nums) and sum(nums)
    # We use binary search to find the smallest sum that is 
    # greater than max(nums) and less than sum(nums)
    def is_valid(nums, k, mid):
        # This function checks if we can split nums into k subarrays
        # such that the sum of each subarray is less than or equal to mid
        # If we can, return True
        # Else, return False
        subarray_sum = 0
        num_subarrays = 1
        for num in nums:
            subarray_sum += num
            if subarray_sum > mid:
                # We have to start a new subarray
                num_subarrays += 1
                subarray_sum = num
                if num_subarrays > k:
                    # We can't split nums into k subarrays
                    return False
        return True
    
    # Initialize the left and right pointers
    left = max(nums)
    right = sum(nums)
    # Binary search
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 10

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    #print(nums, k)
    #print("----------")
    #print("----------")
    #print("----------")
    #print("----------")
