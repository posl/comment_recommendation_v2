Synthesizing 10/10 solutions

=======
Suggestion 1

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        retur

=======
Suggestion 2

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0

=======
Suggestion 3

def maxRotateFunction(nums):
    if len(nums) == 1:
        return 0
    max_sum = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(0, len(nums)):
            sum += (j * nums[(j-i) % len(nums)])
        max_sum = max(max_sum, sum)
    return max_sum

=======
Suggestion 4

def rotation(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        sum += i * nums[i]
    max = sum
    for i in range(1, n):
        sum = sum - n * nums[n - i] + sum
        if sum > max:
            max = sum
    return max

=======
Suggestion 5

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max = -999999999999999999
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[j]
        if sum > max:
            max = sum
        nums = nums[-1:] + nums[:-1]
    return max

=======
Suggestion 6

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0
    max_sum = 0
    for i in range(n):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(n - 1, 0, -1):
        curr_sum += sum(nums) - n * nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum

=======
Suggestion 7

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k = k % l
    if k == 0:
        return nums
    nums[:] = nums[l-k:] + nums[:l-k]
    return nums

=======
Suggestion 8

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    else:
        max_val = 0
        for i in range(len(nums)):
            if i == 0:
                max_val = sum([nums[j]*j for j in range(len(nums))])
            else:
                nums = [nums[-1]] + nums[:-1]
                tmp = sum([nums[j]*j for j in range(len(nums))])
                if tmp > max_val:
                    max_val = tmp
        return max_val

=======
Suggestion 9

def main():
    nums = [4,3,2,6]
    print(rotateFunction(nums))

=======
Suggestion 10

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    s = sum(nums)
    max_val = 0
    for i in range(n):
        max_val += i * nums[i]
    curr = max_val
    for i in range(n-1, 0, -1):
        curr = curr + s - n * nums[i]
        max_val = max(max_val, curr)
    return max_val
