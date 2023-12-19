Synthesizing 10/10 solutions

=======
Suggestion 1

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = 0
    for i in range(len(nums)):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(len(nums)-1, 0, -1):
        curr_sum += sum(nums) - len(nums) * nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
print(maxRotateFunction([-100,100]))
print("The values above should be 26, 0, 330, 0, and 0.")

=======
Suggestion 2

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sumNums = sum(nums)
    F = 0
    n = len(nums)
    for i in range(n):
        F += i*nums[i]
    maxF = F
    for i in range(1,n):
        F = F + sumNums - n*nums[n-i]
        maxF = max(maxF, F)
    return maxF

=======
Suggestion 3

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[(j + i) % len(nums)]
        max_sum = max(max_sum, sum)
    return max_sum

=======
Suggestion 4

def rotate(nums):
    return [nums[-1]] + nums[:-1]

=======
Suggestion 5

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0,nums.pop())

=======
Suggestion 6

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    sums = sum(nums)
    f = 0
    for i in range(n):
        f += i * nums[i]
    maxf = f
    for i in range(1, n):
        f += sums - n * nums[n - i]
        if f > maxf:
            maxf = f
    return maxf

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([]))

=======
Suggestion 7

def maxRotateFunction(nums):
    maxSum = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[(j + i) % len(nums)]
        if sum > maxSum:
            maxSum = sum
    return maxSum

=======
Suggestion 8

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0
    ret = 0
    for i in range(n):
        ret += i * nums[i]
    max_val = ret
    for i in range(1, n):
        ret = ret + sum(nums) - n * nums[n - i]
        max_val = max(ret, max_val)
    return max_val

print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

=======
Suggestion 9

def rotate(nums, k):
    """
    Rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """
    #nums.reverse()
    #nums[:k] = reversed(nums[:k])
    #nums[k:] = reversed(nums[k:])
    k = k % len(nums)
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
    return nums

=======
Suggestion 10

def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum(nums) - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result

    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result

    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result

    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result

    result = 0
    for i in range(0, len(nums)):
        result += i * nums[i]
    sum_nums = sum(nums)
    max_result = result
    for i in range(0, len(nums)):
        result = result + sum_nums - len(nums) * nums[-i-1]
        max_result = max(max_result, result)
    return max_result


print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1
