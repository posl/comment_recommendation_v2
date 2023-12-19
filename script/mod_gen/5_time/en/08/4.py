def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max = -999999999999999999
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[j]
        if sum > max:
            max = sum
        nums = nums[-1:] + nums[:-1]
    return max

if __name__ == '__main__':
    maxRotateFunction()