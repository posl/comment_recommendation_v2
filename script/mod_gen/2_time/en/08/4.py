def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    sum_n = sum(nums)
    f0 = 0
    for i in range(n):
        f0 += i * nums[i]
    max_f = f0
    for i in range(1,n):
        f0 += sum_n - n * nums[n-i]
        max_f = max(max_f,f0)
    return max_f

if __name__ == '__main__':
    maxRotateFunction()