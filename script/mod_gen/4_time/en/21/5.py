def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initialize the result
    result = 0
    # initialize the counter
    counter = 0
    # iterate the input
    for i in range(2, len(nums)):
        # check if the difference is the same
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            # update the counter
            counter += 1
            # update the result
            result += counter
        # otherwise
        else:
            # reset the counter
            counter = 0
    # return the result
    return result

if __name__ == '__main__':
    numberOfArithmeticSlices()