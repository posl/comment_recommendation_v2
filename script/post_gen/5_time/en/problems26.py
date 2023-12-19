Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    n = len(nums)
    dp = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
    sub = [0]
    for num in nums:
        sub.append(sub[-1] + num)
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, min(m, i)+1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
    return dp[n][m]

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,2,3,4,5], 4))
print(splitArray([1,2,3,4,5], 5))
print(splitArray([1,2,3,4,5], 6))
print(splitArray([1,2,3,4,5], 7))
print(splitArray([1,2,3,4,5,6], 7))
print(splitArray([1,2,3,4,5,6], 6))
print(splitArray([1,2,3,4,5,6], 5))
print(splitArray([1,2,3,4,5,6], 4))
print(splitArray([1,2,3,4,5,6], 3))
print(splitArray([1,2,3,4,5,6], 2))
print(splitArray([1,2,3,4,5,6], 1))
print(splitArray([1,2,3,4,5,6], 0))
print(splitArray([1,2,3,4,5,6], 8))
print(splitArray([1,2,3,4,5,6], 9))
print(splitArray([1,2,3,4,5,6], 10))
print(splitArray([1,2,3,4,5,

=======
Suggestion 2

def splitArray(nums, k):
    def isPossible(mid, k):
        cnt = 1
        currSum = 0
        for i in nums:
            currSum += i
            if currSum > mid:
                currSum = i
                cnt += 1
                if cnt > k:
                    return False
        return True

    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if isPossible(mid, k):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8],2))
print(splitArray([1,2,3,4,5],2))
print(splitArray([1,4,4],3))
print(splitArray([1,2,3,4,5],1))

=======
Suggestion 3

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def splitArrayHelper(nums, m, mid):
        count = 1
        currentSum = 0
        for num in nums:
            currentSum += num
            if currentSum > mid:
                currentSum = num
                count += 1
                if count > m:
                    return False
        return True

    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) / 2
        if splitArrayHelper(nums, m, mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 4

def minmax(nums, k):
    def is_valid(mid):
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
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(minmax([7,2,5,10,8], 2))
print(minmax([1,2,3,4,5], 2))
print(minmax([1,4,4], 3))
print(minmax([2,3,1,2,4,3], 5))

=======
Suggestion 5

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # this is a binary search problem
    # the max possible sum is sum(nums)
    # the min possible sum is max(nums)
    # we want to find the minimum possible sum of the largest sum of subarrays
    # we can binary search between max(nums) and sum(nums)
    # if the current sum is too small, we need to increase the max sum
    # if the current sum is too large, we need to decrease the max sum
    # if the current sum is just right, we need to check if we can decrease the max sum
    # we can do this by checking if the number of subarrays we have is less than or equal to m
    # if it is, we can decrease the max sum
    # if it is not, we need to increase the max sum
    # if we reach the point where the max sum and min sum are equal, we can return that sum
    # we can check if the sum is too small or too large by using a helper function
    # the helper function will return the number of subarrays we have if we use the current sum
    # if the number of subarrays is less than or equal to m, we can decrease the max sum
    # if the number of subarrays is greater than m, we can increase the max sum
    # we can start by setting the max sum to the sum of the array and the min sum to the max of the array
    # we can then binary search between the min sum and the max sum
    # if the max sum and min sum are equal, we can return the sum
    # we can check if the sum is too small or too large by using a helper function
    # the helper function will return the number of subarrays we have if we use the current sum
    # if the number of subarrays is less than or equal to m, we can decrease the max sum
    # if the number of subarrays is greater than m, we can increase the max sum
    # we can do this by using a binary search
    # we can start by setting the max sum to the sum of the array and the min sum to the max of the array
    # we can then binary search

=======
Suggestion 6

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, k, target):
        count = 1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > target:
                count += 1
                cur_sum = nums[i]
            if count > k:
                return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

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
    def check(mid):
        cuts = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cuts += 1
                cur_sum = num
        return cuts + 1 <= k

    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))

=======
Suggestion 8

def splitArray(nums, k):
    def check(m):
        cuts = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > m:
                cuts += 1
                current_sum = num
        return cuts + 1 <= k
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

=======
Suggestion 9

def minmax(nums, k):
    def condition(val):
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > val:
                total = num
                count += 1
        return count <= k

    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

nums = [7,2,5,10,8]
k = 2
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 2
print(minmax(nums, k))
nums = [1,4,4]
k = 3
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 5
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 1
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 3
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 4
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 5
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 6
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 7
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 8
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 9
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 10
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 11
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 12
print(minmax(nums, k))
nums = [1,2,3,4,5]
k = 13

=======
Suggestion 10

def splitArray(nums, k):
    def check(mid):
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                count += 1
                curr_sum = num
                if count >= k:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([1,4,4], 2))
print(splitArray([1,4,4], 1))
print(splitArray([1,4,4], 4))
print(splitArray([1,4,4], 5))
print(splitArray([1,2147483647], 2))
print(splitArray([1,2147483647], 1))
print(splitArray([1,2147483647], 3))
print(splitArray([1,2147483647], 4))
print(splitArray([1,2147483647], 5))
print(splitArray([1,2147483647], 6))
print(splitArray([1,2147483647], 7))
print(splitArray([1,2147483647], 8))
print(splitArray([1,2147483647], 9))
print(splitArray([1,2147483647], 10))
print(splitArray([1,2147483647], 11))
print(splitArray([1,2147483647], 12))
print(splitArray([1,2147483647], 13))
print(splitArray([1,2147483647], 14))
print(splitArray([1,2147483647], 15))
print(splitArray([1,2147483647], 16))
print(splitArray([1,2147483647], 17))
print(splitArray([1,2147483647], 18))
print(splitArray([1,2147483647], 19))
print(splitArray([1,2147483647],
