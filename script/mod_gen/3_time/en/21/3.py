def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i + 1] - nums[i] == diff:
            count += 1
        else:
            diff = nums[i + 1] - nums[i]
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()