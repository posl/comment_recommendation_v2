def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        if nums[i] in hash:
            return [hash[nums[i]], i]
        else:
            hash[target - nums[i]] = i
    return []
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
nums = [3,3]
target = 6
print(twoSum(nums, target))
