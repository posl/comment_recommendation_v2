Synthesizing 10/10 solutions

=======
Suggestion 1

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    n = len(nums)
    max_sum = 0
    for i in range(n):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(1, n):
        curr_sum = curr_sum - (n * nums[n - i]) + max_sum
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

=======
Suggestion 2

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum1 = sum(nums)
    maxval = 0
    for i in range(n):
        maxval += i * nums[i]
    for i in range(n):
        maxval = max(maxval, sum1 + maxval - n * nums[n - 1 - i])
    return maxval

nums = [4, 3, 2, 6]
print(maxRotateFunction(nums))

=======
Suggestion 3

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return 0
    max_sum = 0
    for i in range(len(nums)):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(1, len(nums)):
        curr_sum = curr_sum - sum(nums) + len(nums) * nums[i - 1]
        max_sum = max(max_sum, curr_sum)
    return max_sum

=======
Suggestion 4

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum = 0
    F = 0
    for i in range(n):
        sum += nums[i]
        F += i * nums[i]
    max = F
    for i in range(1, n):
        F = F + sum - n * nums[n - i]
        if F > max:
            max = F
    return max

=======
Suggestion 5

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 0
    max_sum = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += (j * nums[j])
        if sum > max_sum:
            max_sum = sum
        nums = nums[-1:] + nums[:-1]
    return max_sum

=======
Suggestion 6

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    sum = 0
    for i in range(len(nums)):
        sum += i*nums[i]
    max = sum
    for i in range(len(nums)-1, 0, -1):
        sum += len(nums)*nums[i] - (nums[i]*(len(nums)-1))
        if sum > max:
            max = sum
    return max

=======
Suggestion 7

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Brute Force
    #O(n^2)
    #O(1)
    max_val = -float("inf")
    for i in range(len(nums)):
        val = 0
        for j in range(len(nums)):
            val += j*nums[(j+i)%len(nums)]
        max_val = max(max_val, val)
    return max_val

=======
Suggestion 8

def rotate(arr, k):
    k = k % len(arr)
    arr = arr[-k:] + arr[:-k]
    return arr

=======
Suggestion 9

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    F = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            F[i] += j * nums[(j - i) % len(nums)]
    return max(F)

=======
Suggestion 10

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max_sum = 0
    for i in range(0, len(nums)):
        max_sum += nums[i] * i
    for i in range(0, len(nums)):
        temp_sum = 0
        for j in range(0, len(nums)):
            temp_sum += nums[j] * ((i + j + 1) % len(nums))
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
