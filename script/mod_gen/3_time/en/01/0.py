def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]
    return []
nums = [3,2,4]
target = 6
print(twoSum(nums, target))