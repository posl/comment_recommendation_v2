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
