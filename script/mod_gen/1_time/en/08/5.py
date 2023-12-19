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
