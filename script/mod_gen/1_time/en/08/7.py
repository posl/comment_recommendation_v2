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
