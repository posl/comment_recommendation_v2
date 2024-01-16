Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

=======
Suggestion 2

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Brute Force
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if nums[i]+nums[j]==target:
        #            return [i,j]
        #return [-1,-1]
        
        #Two-pass Hash Table
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        #hash_dict={}
        #for i in range(len(nums)):
        #    hash_dict[nums[i]]=i
        #for i in range(len(nums)):
        #    if target-nums[i] in hash_dict and hash_dict[target-nums[i]]!=i:
        #        return [i,hash_dict[target-nums[i]]]
        #return [-1,-1]
        
        #One-pass Hash Table
        #Time Complexity: O(n)
        #Space Complexity: O(n)
        hash_dict={}
        for i in range(len(nums)):
            if target-nums[i] in hash_dict:
                return [hash_dict[target-nums[i]],i]
            else:
                hash_dict[nums[i]]=i
        return [-1,-1]

=======
Suggestion 3

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return []

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        return []

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        
        # Hash Table
        # hash_table = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hash_table:
        #         hash_table[nums[i]] = i
        #     if target - nums[i] in hash_table:
        #         if hash_table[target - nums[i]] != i:
        #             return [i, hash_table[target - nums[i]]]
        # return []
        
        # One-pass Hash Table
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [i, hash_table[target - nums[i]]]
            hash_table[nums[i]] = i
        return []

=======
Suggestion 8

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                if n + m == target:
                    return [i, j+i+1]
        return []

=======
Suggestion 9

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target-nums[i] == nums[j]:
                    return [i, j]
        return []
