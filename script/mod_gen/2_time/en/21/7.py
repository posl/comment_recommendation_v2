def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    countTemp = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            countTemp += 1
        else:
            diff = nums[i] - nums[i-1]
            countTemp = 2
        if countTemp >= 3:
            count += countTemp - 2
    return count
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([7,7,7,7]))
print(numberOfArithmeticSlices([3,-1,-5,-9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
