def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    length = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            length += 1
        else:
            diff = nums[i] - nums[i-1]
            if length >= 3:
                count += (length-1)*(length-2)/2
            length = 2
    if length >= 3:
        count += (length-1)*(length-2)/2
    return int(count)
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14, 15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,
