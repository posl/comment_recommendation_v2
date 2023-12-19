Synthesizing 10/10 solutions

=======
Suggestion 1

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i,j]
    return []

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

=======
Suggestion 2

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    return [i, j]

=======
Suggestion 3

def twoSum(nums, target):
    # Create a dictionary to store the numbers and their indices
    my_dict = {}
    # Loop through the list of numbers
    for index, num in enumerate(nums):
        # Check if the number in the dictionary
        if num in my_dict:
            # Return the indices
            return [my_dict[num], index]
        # If the number not in the dictionary
        else:
            # Store the number and its index in the dictionary
            my_dict[target - num] = index

=======
Suggestion 4

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

=======
Suggestion 5

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
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

=======
Suggestion 7

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

=======
Suggestion 8

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i!=j) and (nums[i]+nums[j]==target):
                return [i,j]
    return None

=======
Suggestion 9

def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        if nums[i] in hash:
            return [hash[nums[i]], i]
        else:
            hash[target - nums[i]] = i
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
Suggestion 10

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
