def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        return 0
    res = 0
    for i in range(n):
        res += i * nums[i]
    max_sum = res
    for i in range(1, n):
        res = res + sum(nums) - n * nums[-i]
        max_sum = max(max_sum, res)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()