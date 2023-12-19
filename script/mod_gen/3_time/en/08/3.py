def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += (i * nums[i])
        sum2 += nums[i]
    max_sum = sum1
    for i in range(1, n):
        sum1 += (sum2 - (n * nums[n - i]))
        max_sum = max(max_sum, sum1)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()