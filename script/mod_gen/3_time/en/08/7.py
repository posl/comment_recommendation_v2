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
