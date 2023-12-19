def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0
    max_sum = 0
    for i in range(n):
        max_sum += i * nums[i]
    sum_prev = max_sum
    for i in range(1, n):
        sum_prev -= n * nums[n-i]
        sum_prev += sum(nums[:i])
        max_sum = max(max_sum, sum_prev)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()