Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(0, len(nums)-2):
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                count += 1
            else:
                break
    return count

=======
Suggestion 2

def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+1,len(nums)-1):
            if nums[j+1] - nums[j] == diff:
                count += 1
            else:
                break
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,8,10,12,14,16,18,20,22,24,26,28,30]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,8,10,12,14,16,18,20,22,24,26,28,30,31]))

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #numOfSubarrays = 0
    #for i in range(0,len(nums)-2):
    #    for j in range(i+2,len(nums)):
    #        diff = nums[i+1] - nums[i]
    #        if nums[j] - nums[j-1] == diff:
    #            numOfSubarrays += 1
    #        else:
    #            break
    #return numOfSubarrays

    #Solution 2
    numOfSubarrays = 0
    for i in range(0,len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2,len(nums)):
            if nums[j] - nums[j-1] == diff:
                numOfSubarrays += 1
            else:
                break
    return numOfSubarrays

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                count += 1
            else:
                break
    return count

nums = [1,2,3,4]
print(numberOfArithmeticSlices(nums))
nums = [1]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(numberOfArithmeticSlices

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0

    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count

print(numberOfArithmeticSlices([1, 2, 3, 4]))
print(numberOfArithmeticSlices([1]))

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        diff = nums[j] - nums[i]
        while j < len(nums) - 1:
            if nums[j + 1] - nums[j] == diff:
                count += 1
                j += 1
            else:
                break
        i += 1
    return count

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(nums)-2):
        for j in range(i+2, len(nums)):
            diff = nums[i+1] - nums[i]
            if nums[j] - nums[j-1] == diff:
                res += 1
            else:
                break
    return res

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(numberOfArithmeticSlices([1

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [0] * len(nums)
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1
    return sum(dp)

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
