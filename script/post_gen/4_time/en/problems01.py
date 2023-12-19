Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

    return None

=======
Suggestion 2

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

=======
Suggestion 3

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

=======
Suggestion 4

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return[i,j]
    return[]

nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))

=======
Suggestion 5

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

nums = [3,2,4]
target = 6
print(twoSum(nums,target))

nums = [3,3]
target = 6
print(twoSum(nums,target))

=======
Suggestion 6

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
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
Suggestion 7

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    # Solution 1: Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    #for i in range(len(nums)):
    #    for j in range(i+1, len(nums)):
    #        if nums[i] + nums[j] == target:
    #            return [i,j]
    #return []
    
    # Solution 2: Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #hash_table = {}
    #for i in range(len(nums)):
    #    hash_table[nums[i]] = i
    #for i in range(len(nums)):
    #    complement = target - nums[i]
    #    if complement in hash_table and hash_table[complement] != i:
    #        return [i, hash_table[complement]]
    #return []
    
    # Solution 3: Hash Table
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i
    return []
    
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
