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
    maxVal = 0
    for i in range(len(nums)):
        maxVal += i * nums[i]
    maxValTemp = maxVal
    for i in range(len(nums) - 1, 0, -1):
        maxValTemp = maxValTemp + sum(nums) - len(nums) * nums[i]
        maxVal = max(maxVal, maxValTemp)
    return maxVal

=======
Suggestion 2

def rotateArray(nums, k):
    if k == 0:
        return nums
    elif k > 0:
        for i in range(k):
            nums.insert(0, nums.pop())
        return nums
    else:
        for i in range(abs(k)):
            nums.append(nums.pop(0))
        return nums

=======
Suggestion 3

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1].
    #F(k+1) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0].
    #F(k+1) - F(k) = 0 * arr_k[1] + 1 * arr_k[2] + ... + (n - 1) * arr_k[0] - 0 * arr_k[0] - 1 * arr_k[1] - ... - (n - 1) * arr_k[n - 1] = 0 * (arr_k[1] - arr_k[0]) + 1 * (arr_k[2] - arr_k[1]) + ... + (n - 1) * (arr_k[0] - arr_k[n - 1])
    #F(k+1) - F(k) = arr_k[1] - arr_k[0] + arr_k[2] - arr_k[1] + ... + arr_k[0] - arr_k[n - 1] = arr_k[0] - arr_k[n - 1]
    #F(k+1) = F(k) + sum(arr) - n * arr_k[n - 1]
    if not nums:
        return 0
    n = len(nums)
    f0 = sum(i * nums[i] for i in range(n))
    s = sum(nums)
    res = f0
    for i in range(1, n):
        f0 += s - n * nums[n - i]
        res = max(res, f0)
    return res

=======
Suggestion 4

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0 or len(nums) == 1:
        return
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

=======
Suggestion 5

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum_n = sum(nums)
    f0 = 0
    for i in range(n):
        f0 += i * nums[i]
    max_f = f0
    for i in range(1,n):
        f0 += sum_n - n * nums[n-i]
        max_f = max(max_f,f0)
    return max_f

=======
Suggestion 6

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = [0]*len(nums)
    for i in range(len(nums)):
        temp[(i+k)%len(nums)] = nums[i]
    for i in range(len(nums)):
        nums[i] = temp[i]

=======
Suggestion 7

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sm = sum(nums)
    F = [0]*n
    F[0] = sum([i*nums[i] for i in range(n)])
    for i in range(1,n):
        F[i] = F[i-1] + sm - n*nums[n-i]
    return max(F)

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))

=======
Suggestion 8

def maxRotateFunction(nums):
    n = len(nums)
    sum_all = sum(nums)
    F = 0
    for i in range(n):
        F += i*nums[i]
    max_F = F
    for i in range(1, n):
        F = F + sum_all - n*nums[n-i]
        if F > max_F:
            max_F = F
    return max_F

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
    n = len(nums)
    if n == 1:
        return 0
    max_sum = 0
    for i in range(n):
        max_sum += i * nums[i]
    sum_prev = max_sum
    for i in range(1, n):
        sum_prev -= n * nums[n-i]
        sum_prev += sum(nums[:i])
        max_sum = max(max_sum, sum_prev)
    return max_sum

=======
Suggestion 10

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxVal = 0
    for i in range(len(nums)):
        maxVal += i * nums[i]
    sumVal = maxVal
    for i in range(len(nums)-1,0,-1):
        sumVal += sum(nums) - len(nums) * nums[i]
        maxVal = max(maxVal, sumVal)
    return maxVal
print(maxRotateFunction([4,3,2,6])) #26
print(maxRotateFunction([100])) #0
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10])) #330
print(maxRotateFunction([-2147483648,-2147483648])) #0
print(maxRotateFunction([2147483647,2147483647])) #0
print(maxRotateFunction([2147483647,-2147483648])) #0
print(maxRotateFunction([2147483647,-2147483648,2147483647])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647,-2147483648])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647,-2147483648,2147483647])) #2147483647
print
