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
