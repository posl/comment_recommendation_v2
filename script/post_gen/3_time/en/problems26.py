Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # 1. find the min and max of the array
    # 2. use binary search to find the min max sum
    # 3. check if the sum is valid
    # 4. return the min max sum
    # 5. check if the sum is valid
    # 6. return the min max sum
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    minSum = max(nums)
    maxSum = sum(nums)
    def isValid(mid):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                count += 1
                currSum = num
                if count > m:
                    return False
        return True
    while minSum < maxSum:
        mid = (minSum + maxSum) // 2
        if isValid(mid):
            maxSum = mid
        else:
            minSum = mid + 1
    return minSum
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([2,3,1,2,4,3], 5))
print(splitArray([1,2147483647], 2))
print("The values above should be 18, 9, 4, 4, and 2147483647.")

=======
Suggestion 2

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # O(N log N)
    # binary search for the minimum largest sum
    # initialize the bounds
    left = max(nums)
    right = sum(nums)
    
    # binary search
    while left < right:
        mid = left + (right - left) // 2
        
        # greedy split
        pieces = 1
        curr_sum = 0
        for num in nums:
            if curr_sum + num > mid:
                pieces += 1
                curr_sum = num
            else:
                curr_sum += num
        
        if pieces > m:
            left = mid + 1
        else:
            right = mid
    
    return left

=======
Suggestion 3

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return 0

print(splitArray([7,2,5,10,8], 2)) #18
print(splitArray([1,2,3,4,5], 2)) #9

=======
Suggestion 4

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        count = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                curr_sum = num
                count += 1
                if count > k:
                    return False
        return True
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) / 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print("The values above should be 18, 9, and 4.")

=======
Suggestion 5

def minmax(nums, k):
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if feasible(nums, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 6

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isPossible(maxSum):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > maxSum:
                currSum = num
                count += 1
                if count > k:
                    return False
        return True
    
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))

=======
Suggestion 7

def split_array(nums,k):
    def split_array_helper(nums, k, start, end, memo):
        if (start, end, k) in memo:
            return memo[(start, end, k)]
        if k == 1:
            return sum(nums[start:end+1])
        if start == end:
            return nums[start]
        min_split = float("inf")
        for i in range(start, end):
            min_split = min(min_split, max(split_array_helper(nums, k-1, start, i, memo), sum(nums[i+1:end+1])))
        memo[(start, end, k)] = min_split
        return min_split
    return split_array_helper(nums, k, 0, len(nums)-1, {})

print(split_array([7,2,5,10,8], 2))
print(split_array([1,2,3,4,5], 2))
print(split_array([1,4,4], 3))

=======
Suggestion 8

def splitArray(nums, k):
    pass

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums, k))

=======
Suggestion 9

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        cuts = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cuts += 1
                curr_sum = num
        return cuts + 1
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if check(mid) <= k:
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))

=======
Suggestion 10

def splitArray(self, nums: List[int], k: int) -> int:
    # Time: O(nlog(sum of nums))
    # Space: O(1)
    # Binary search on the answer. The answer lies between the max element and the sum of all elements
    # We need to find the min sum of subarrays such that the number of subarrays is equal to k
    # We can use binary search to find the answer. We can use the greedy approach to find the min sum of subarrays
    # We can check if the mid value is possible or not. If it is possible, we can try to find a better answer
    # If it is not possible, we can increase the mid value
    # The answer will be the minimum value of mid such that it is possible to get k subarrays
    # We can use a greedy approach to check if the mid value is possible or not
    # We can keep a track of the sum of the subarray and the number of subarrays
    # If the sum of the subarray exceeds the mid value, we can increase the number of subarrays
    # We can also check if the number of subarrays is greater than k or not
    # If the number of subarrays is greater than k, we can return False
    # If the number of subarrays is less than or equal to k, we can return True
    def isPossible(mid, k):
        subarraySum = 0
        subarrays = 1
        for num in nums:
            subarraySum += num
            if subarraySum > mid:
                subarraySum = num
                subarrays += 1
                if subarrays > k:
                    return False
        return True
    low = max(nums)
    high = sum(nums)
    while low < high:
        mid = low + (high - low) // 2
        if isPossible(mid, k):
            high = mid
        else:
            low = mid + 1
    return low
