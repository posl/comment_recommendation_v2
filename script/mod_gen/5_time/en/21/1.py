def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+1,len(nums)-1):
            if nums[j+1] - nums[j] == diff:
                count += 1
            else:
                break
    return count
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
