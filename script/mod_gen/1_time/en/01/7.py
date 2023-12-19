def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([3,2,3], 6))
print(twoSum([3,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 26))
