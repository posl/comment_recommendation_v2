def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max_sum = 0
    for i in range(0, len(nums)):
        max_sum += nums[i] * i
    for i in range(0, len(nums)):
        temp_sum = 0
        for j in range(0, len(nums)):
            temp_sum += nums[j] * ((i + j + 1) % len(nums))
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
