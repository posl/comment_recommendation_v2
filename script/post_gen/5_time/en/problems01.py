Synthesizing 10/10 solutions

=======
Suggestion 1

def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 2

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

nums=[3,2,4]
target=6
print(twoSum(nums,target))

=======
Suggestion 3

def twoSum(nums, target):
    index = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
    return index

=======
Suggestion 4

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i]+nums[j] == target:
                return [i,j]


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

=======
Suggestion 5

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i,j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 6

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]
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

=======
Suggestion 7

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                print([i, j])
                return [i, j]

=======
Suggestion 8

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

=======
Suggestion 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j] == target):
                return [i,j]
    return []

=======
Suggestion 10

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
