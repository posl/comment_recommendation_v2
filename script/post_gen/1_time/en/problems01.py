Synthesizing 10/10 solutions

=======
Suggestion 1

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

=======
Suggestion 2

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i,j]
        return []

=======
Suggestion 3

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

=======
Suggestion 4

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Brute force
        #for i in range(0,len(nums)):
        #    for j in range(i+1,len(nums)):
        #        if(nums[i]+nums[j]==target):
        #            return [i,j]
        #return [-1,-1]
        
        #Hash table
        #hashmap = {}
        #for i in range(0,len(nums)):
        #    if(target-nums[i] in hashmap):
        #        return [hashmap.get(target-nums[i]),i]
        #    hashmap[nums[i]]=i
        #return [-1,-1]
        
        #Two pointer
        nums = [(v,i) for i,v in enumerate(nums)]
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<j):
            if(nums[i][0]+nums[j][0]==target):
                return [nums[i][1],nums[j][1]]
            elif(nums[i][0]+nums[j][0]<target):
                i+=1
            else:
                j-=1
        return [-1,-1]

=======
Suggestion 5

def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # Hashmap solution
        # nums_map = {}
        # for i, num in enumerate(nums):
        #     nums_map[num] = i
        
        # for i, num in enumerate(nums):
        #     if target - num in nums_map and i != nums_map[target - num]:
        #         return [i, nums_map[target - num]]
        
        # One-pass Hash Table
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [i, nums_map[target - num]]
            
            nums_map[num] = i
        
        return []

=======
Suggestion 6

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

=======
Suggestion 7

def twoSum(self, nums: list[int], target: int) -> list[int]:
        #print("nums: ", nums)
        #print("target: ", target)
        for i in range(0, len(nums)):
            #print("i: ", i)
            for j in range(i+1, len(nums)):
                #print("j: ", j)
                if nums[i] + nums[j] == target:
                    #print("nums[i]: ", nums[i])
                    #print("nums[j]: ", nums[j])
                    #print("nums[i]+nums[j]: ", nums[i]+nums[j])
                    return [i, j]
        return []

=======
Suggestion 8

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        return []

=======
Suggestion 9

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                else:
                    continue
        return []

=======
Suggestion 10

def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    else:
                        continue
        return []
