Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(self, nums: List[int], k: int) -> int:
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
Suggestion 2

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def isPossible(nums, k, mid):
        current_sum = 0
        splits = 1
        for num in nums:
            current_sum += num
            if current_sum > mid:
                splits += 1
                current_sum = num
                if splits > k:
                    return False
        return True
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if isPossible(nums, k, mid):
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
    def is_valid(nums, k, mid):
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
    
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = (left + right) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left
    
print(splitArray([7,2,5,10,8], 2))

=======
Suggestion 4

def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def isPossible(mid, m, nums):
        count = 1
        sum = 0
        for num in nums:
            sum += num
            if sum > mid:
                count += 1
                sum = num
        return count <= m
    
    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = l + (r - l)//2
        if isPossible(mid, m, nums):
            r = mid
        else:
            l = mid + 1
    return l
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print("The values above should be 18, 9, and 4.")

=======
Suggestion 5

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, mid, k):
        cnt = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                cnt += 1
                curr_sum = num
                if cnt > k:
                    return False
        return True
    
    low = max(nums)
    high = sum(nums)
    while low <= high:
        mid = low + (high-low)//2
        if is_valid(nums, mid, k):
            high = mid - 1
        else:
            low = mid + 1
    return low

print(splitArray([7,2,5,10,8], 2)) #18

=======
Suggestion 6

def splitArray(nums, k):
    def isPossible(m):
        cnt = 0
        curr = 0
        for x in nums:
            if curr + x > m:
                cnt += 1
                curr = x
            else:
                curr += x
        return cnt + 1 <= k

    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        if isPossible(mid):
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
print(splitArray([1,2147483647], 2))

=======
Suggestion 7

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], sum(nums[l:j])))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][

=======
Suggestion 8

def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def is_valid(nums, k, target):
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total > target:
                total = nums[i]
                count += 1
        count += 1
        return count <= k
    
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
print(splitArray([

=======
Suggestion 9

def splitArray(nums, k):
    pass

=======
Suggestion 10

def splitArray(nums, k):
    def valid(mid):
        total, cnt = 0, 1
        for num in nums:
            total += num
            if total > mid:
                total = num
                cnt += 1
                if cnt > k:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if valid(mid):
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
