Synthesizing 10/10 solutions

=======
Suggestion 1

def arithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count

nums = [1,2,3,4]
print(arithmeticSlices(nums))

=======
Suggestion 2

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(0, len(nums)-2):
        j = i + 1
        diff = nums[j] - nums[i]
        while j < len(nums)-1 and nums[j+1] - nums[j] == diff:
            count += 1
            j += 1
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        diff = nums[i+1] - nums[i]
        for j in range(i+1, len(nums)-1):
            if nums[j+1] - nums[j] == diff:
                count += 1
            else:
                break
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))

=======
Suggestion 4

def arithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1]-nums[i]==nums[i+2]-nums[i+1]:
            count += 1
            j = 3
            while i+j<len(nums) and nums[i+j]-nums[i+j-1]==nums[i+1]-nums[i]:
                count += 1
                j += 1
    return count

print(arithmeticSlices([1,2,3,4]))
print(arithmeticSlices([1]))
print(arithmeticSlices([1,2,3,4,5,6]))
print(arithmeticSlices([1,2,3,4,5,6,7]))
print("The values above should be 3, 0, 10, and 15.")

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0

    diff = nums[1] - nums[0]
    count = 0
    res = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            count += 1
            res += count
        else:
            diff = nums[i] - nums[i-1]
            count = 0
    return res

=======
Suggestion 6

def arithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1st approach
    # DP solution
    # Time complexity: O(n)
    # Space complexity: O(n)
    # dp = [0] * len(nums)
    # for i in range(2, len(nums)):
    #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
    #         dp[i] = dp[i-1] + 1
    # return sum(dp)

    # 2nd approach
    # Time complexity: O(n)
    # Space complexity: O(1)
    count = 0
    curr = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            curr += 1
            count += curr
        else:
            curr = 0
    return count

=======
Suggestion 7

def slices(nums):
    count = 0
    for i in range(len(nums)-2):
        if nums[i+2] - nums[i+1] == nums[i+1] - nums[i]:
            count += 1
    return count

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    countTemp = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            countTemp += 1
        else:
            diff = nums[i] - nums[i-1]
            countTemp = 2
        if countTemp >= 3:
            count += countTemp - 2
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([7,7,7,7]))
print(numberOfArithmeticSlices([3,-1,-5,-9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    else:
        count = 0
        for i in range(0, len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    total = 0
    i = 0
    while i < len(nums) - 2:
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count = 3
            j = i + 3
            while j < len(nums) and nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                count += 1
                j += 1
            total += (count - 2) * (count - 1) // 2
            i = j - 1
        else:
            i += 1
    return total
