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
    curr_sum = max_sum
    for i in range(n - 1, 0, -1):
        curr_sum += sum(nums) - n * nums[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()