Synthesizing 10/10 solutions

=======
Suggestion 1

def maxRotateFunction(nums):
    if len(nums) == 1:
        return 0
    else:
        max = 0
        for i in range(len(nums)):
            f = 0
            for j in range(len(nums)):
                f += j * nums[j - i]
            if f > max:
                max = f
        return max

=======
Suggestion 2

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    s = sum(nums)
    f = sum([i*nums[i] for i in range(n)])
    m = f
    for i in range(n-1,0,-1):
        f = f + s - n*nums[i]
        m = max(m,f)
    return m

nums = [4,3,2,6]
print(maxRotateFunction(nums))

=======
Suggestion 3

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
    maxF = F
    for i in range(1, n):
        F = F + sum - n * nums[n - i]
        maxF = max(F, maxF)
    return maxF

=======
Suggestion 4

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += (i * nums[i])
        sum2 += nums[i]
    max_sum = sum1
    for i in range(1, n):
        sum1 += (sum2 - (n * nums[n - i]))
        max_sum = max(max_sum, sum1)
    return max_sum

=======
Suggestion 5

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0

    res = 0
    for i in range(n):
        res += i * nums[i]

    max_sum = res
    for i in range(1, n):
        res = res + sum(nums) - n * nums[-i]
        max_sum = max(max_sum, res)

    return max_sum

=======
Suggestion 6

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

=======
Suggestion 7

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0
    max_val = 0
    for i in range(n):
        max_val += nums[i] * i
    cur_val = max_val
    sum_val = sum(nums)
    for i in range(n-1, 0, -1):
        cur_val = cur_val + sum_val - nums[i] * n
        max_val = max(max_val, cur_val)
    return max_val

=======
Suggestion 8

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
    for i in range(n-1, 0, -1):
        F = F + sum - n * nums[i]
        if F > max:
            max = F
    return max

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))

=======
Suggestion 9

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1]
    # F(k+1) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0]
    # F(k+1) = F(k) + sum(array) - n * arr_k[n-1]
    # F(k+1) - F(k) = sum(array) - n * arr_k[n-1]
    # F(k+1) = F(k) + sum(array) - n * arr_k[n-1]
    # F(k) = F(k-1) + sum(array) - n * arr_k[n-1]
    # F(k) = F(k-1) + sum(array) - n * arr_k[n-1]
    # F(k-1) = F(k-2) + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) - n * arr_k[n-2]
    # F(k) = F(k-2) + sum(array) - n * arr_k[n-1] + sum(array) -

=======
Suggestion 10

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    else:
        max_sum = 0
        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(0, len(nums)):
                current_sum += j*nums[(j+i)%len(nums)]
            max_sum = max(max_sum, current_sum)
        return max_sum

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
print(maxRotateFunction([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]))
print(maxRotateFunction([-1,2,-3,4,-5,6,-7,8,-9,10]))
