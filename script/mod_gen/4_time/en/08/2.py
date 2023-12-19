def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return 0
    max_sum = 0
    for i in range(len(nums)):
        max_sum += i * nums[i]
    curr_sum = max_sum
    for i in range(1, len(nums)):
        curr_sum = curr_sum - sum(nums) + len(nums) * nums[i - 1]
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == '__main__':
    maxRotateFunction()