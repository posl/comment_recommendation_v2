def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        if target-n in d:
            return [d[target-n], i]
        else:
            d[n] = i
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
