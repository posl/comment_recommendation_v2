def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    else:
        max_sum = 0
        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(0, len(nums)):
                current_sum += j*nums[(j+i)%len(nums)]
            max_sum = max(max_sum, current_sum)
        return max_sum
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
print(maxRotateFunction([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]))
print(maxRotateFunction([-1,2,-3,4,-5,6,-7,8,-9,10]))
