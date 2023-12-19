def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum = 0
    F = 0
    for i in range(n):
        sum += nums[i]
        F += i * nums[i]
    max = F
    for i in range(1, n):
        F = F + sum - n * nums[n - i]
        if F > max:
            max = F
    return max

if __name__ == '__main__':
    maxRotateFunction()