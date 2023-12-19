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
