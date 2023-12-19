def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 0
    max_sum = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += (j * nums[j])
        if sum > max_sum:
            max_sum = sum
        nums = nums[-1:] + nums[:-1]
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()