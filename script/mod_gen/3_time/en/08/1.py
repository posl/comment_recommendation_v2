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
