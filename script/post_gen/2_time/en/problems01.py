Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(nums, target):
    """Return indices of the two numbers such that they add up to target.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return 0

=======
Suggestion 2

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 3

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

=======
Suggestion 4

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 5

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

=======
Suggestion 6

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]
    return None

=======
Suggestion 7

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
Suggestion 8

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
