Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

=======
Suggestion 2

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]
        return []

=======
Suggestion 3

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            if target-num in nums[i+1:]:
                return [i, nums[i+1:].index(target-num)+(i+1)]

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j]  == target:
                    return [i, j]
        
        # Hash Table
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target - nums[i]], i]
            hash_table[nums[i]] = i

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return []

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        return []
