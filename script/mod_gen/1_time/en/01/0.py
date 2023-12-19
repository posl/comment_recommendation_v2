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

if __name__ == '__main__':
    twoSum()