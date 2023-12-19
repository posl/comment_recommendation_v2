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

if __name__ == '__main__':
    maxRotateFunction()