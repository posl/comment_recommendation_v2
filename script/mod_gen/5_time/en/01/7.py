def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
nums = [3,3]
target = 6
print(twoSum(nums, target))
