def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    sum = 0
    for i in range(len(nums)):
        sum += i*nums[i]
    max = sum
    for i in range(len(nums)-1, 0, -1):
        sum += len(nums)*nums[i] - (nums[i]*(len(nums)-1))
        if sum > max:
            max = sum
    return max

if __name__ == '__main__':
    maxRotateFunction()