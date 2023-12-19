def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    n = len(nums)
    max_sum = 0
    for i in range(n):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(1, n):
        curr_sum = curr_sum - (n * nums[n - i]) + max_sum
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()