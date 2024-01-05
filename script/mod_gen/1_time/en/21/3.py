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

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)