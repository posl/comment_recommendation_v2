Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    count = 0
    sum = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            count += 1
            sum += count
        else:
            count = 0

    return sum

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
    diff = nums[1] - nums[0]
    length = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == diff:
            length += 1
        else:
            diff = nums[i] - nums[i-1]
            if length >= 3:
                count += (length-1)*(length-2)/2
            length = 2

    if length >= 3:
        count += (length-1)*(length-2)/2

    return int(count)

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14, 15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16, 17]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1
    # Time:  O(n)
    # Space: O(1)
    #dp = [0] * len(nums)
    #for i in range(2, len(nums)):
    #    if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
    #        dp[i] = dp[i - 1] + 1
    #return sum(dp)

    # Solution 2
    # Time:  O(n)
    # Space: O(1)
    result, count = 0, 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            count += 1
            result += count
        else:
            count = 0
    return result

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0
    count = 0
    diff = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        if nums[i + 1] - nums[i] == diff:
            count += 1
        else:
            diff = nums[i + 1] - nums[i]
    return count

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    count = 0
    for i in range(len(nums)-2):
        a = nums[i+1] - nums[i]
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == a:
                count += 1
            else:
                break
    return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count += 1
            j = 3
            while i+j < len(nums) and nums[i+j] - nums[i+j-1] == nums[i+1] - nums[i]:
                count += 1
                j += 1
    return count

=======
Suggestion 7

def arithmeticSlices(nums):
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count += 1
            j = 3
            while i+j < len(nums) and nums[i+j] - nums[i+j-1] == nums[i+1] - nums[i]:
                count += 1
                j += 1
    return count

nums = [1, 2, 3, 4]
print(arithmeticSlices(nums))
nums = [1]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20, 21]
print(arithmeticSlices(nums))
nums = [1, 3, 5, 7, 9]
print(arithmeticSlices(nums))
nums = [7, 7, 7, 7]
print(arithmetic

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(0, len(nums)-2):
        for j in range(i+2, len(nums)):
            if (nums[i+1]-nums[i]) == (nums[j]-nums[j-1]):
                count += 1
            else:
                break
    return count

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    result = 0
    for i in range(len(nums)):
        for j in range(i+2, len(nums)+1):
            if all(nums[k+1]-nums[k] == nums[i+1]-nums[i] for k in range(i+1, j-1)):
                result += 1
    return result

print(numberOfArithmeticSlices([1,2,3,4]))

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initialize the number of arithmetic slices
    n = len(nums)
    result = 0
    # initialize the dp array
    dp = [0] * n
    # loop through the array
    for i in range(2, n):
        # check if the difference between the current element and the previous element is equal to the difference between the previous element and the element before it
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            # if it is, then add the previous number of arithmetic slices to the current number of arithmetic slices
            dp[i] = dp[i - 1] + 1
        # add the current number of arithmetic slices to the total number of arithmetic slices
        result += dp[i]
    # return the total number of arithmetic slices
    return result
