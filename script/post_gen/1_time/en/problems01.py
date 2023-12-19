Synthesizing 10/10 solutions

=======
Suggestion 1

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """    
    #Brute Force
    #Time Complexity: O(n^2)
    #Space Complexity: O(1)
    #for i in range(len(nums)):
    #    for j in range(i+1,len(nums)):
    #        if nums[i] + nums[j] == target:
    #            return [i,j]
    #return []
    
    #Hash Table
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    hashTable = {}
    for i in range(len(nums)):
        if target - nums[i] in hashTable:
            return [hashTable[target-nums[i]],i]
        hashTable[nums[i]] = i
    return []

=======
Suggestion 2

def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j] == target):
                return [i, j]
    return []

=======
Suggestion 3

def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 4

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print(i,j)

twoSum([2,7,11,15],9)
twoSum([3,2,4],6)
twoSum([3,3],6)

=======
Suggestion 5

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

=======
Suggestion 6

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return None

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 7

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i,j]

=======
Suggestion 8

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

=======
Suggestion 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 10

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
