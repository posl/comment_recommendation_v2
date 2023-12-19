def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    maxVal = 0
    for i in range(len(nums)):
        maxVal += i * nums[i]
    maxValTemp = maxVal
    for i in range(len(nums) - 1, 0, -1):
        maxValTemp = maxValTemp + sum(nums) - len(nums) * nums[i]
        maxVal = max(maxVal, maxValTemp)
    return maxVal

if __name__ == '__main__':
    maxRotateFunction()