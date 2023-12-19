Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0

    dp = [0] * len(nums)
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1

    return sum(dp)

=======
Suggestion 2

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        for j in range(i+1, len(nums)-1):
            if nums[j+1] - nums[j] == diff:
                res += 1
            else:
                break
    return res

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
        for j in range(i+2, len(nums)):
            if nums[j] - nums[j-1] == diff:
                count += 1
            else:
                break
    return count

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initialize the output
    output = 0
    # initialize the length of the array
    length = len(nums)
    # initialize the current count
    currentCount = 0
    # iterate the array
    for i in range(2, length):
        # if the difference between the previous two elements is equal to the difference between the current two elements
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            # increment the current count by 1
            currentCount += 1
            # increment the output by the current count
            output += currentCount
        # otherwise
        else:
            # reset the current count to 0
            currentCount = 0
    # return the output
    return output

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count += 1
            for j in range(i+3, len(nums)):
                if nums[j] - nums[j-1] == nums[i+1] - nums[i]:
                    count += 1
                else:
                    break
    return count

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
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i:j+1] == sorted(nums[i:j+1])):
                count += 1
    return count

nums = [1,2,3,4]
print(numberOfArithmeticSlices(nums))
nums = [1]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #if len(nums) < 3:
    #    return 0
    #count = 0
    #for i in range(0, len(nums)-2):
    #    diff = nums[i+1] - nums[i]
    #    for j in range(i+1, len(nums)-1):
    #        if nums[j+1] - nums[j] == diff:
    #            count += 1
    #        else:
    #            break
    #return count
    
    #Solution 2
    #if len(nums) < 3:
    #    return 0
    #count = 0
    #for i in range(0, len(nums)-2):
    #    diff = nums[i+1] - nums[i]
    #    for j in range(i+1, len(nums)-1):
    #        if nums[j+1] - nums[j] == diff:
    #            count += 1
    #        else:
    #            break
    #return count
    
    #Solution 3
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(0, len(nums)-2):
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
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print("The values above should be 3, 0, 10, 25, and 35.")

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    diff = nums[1] - nums[0]
    count = 0
    slice_len = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == diff:
            slice_len += 1
        else:
            if slice_len > 2:
                count += (slice_len - 1) * (slice_len - 2) / 2
            diff = nums[i] - nums[i - 1]
            slice_len = 2
    if slice_len > 2:
        count += (slice_len - 1) * (slice_len - 2) / 2
    return int(count)

=======
Suggestion 9

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

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums) - 2):
        diff = nums[i + 1] - nums[i]
        for j in range(i + 2, len(nums)):
            if nums[j] - nums[j - 1] == diff:
                count += 1
            else:
                break
    return count
