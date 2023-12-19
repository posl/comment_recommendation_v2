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

if __name__ == '__main__':
    maxRotateFunction()