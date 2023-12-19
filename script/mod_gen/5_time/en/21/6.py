def numberOfArithmeticSlices(nums):
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count
print(numberOfArithmeticSlices([1, 2, 3, 4]))
print(numberOfArithmeticSlices([1]))
