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

if __name__ == '__main__':
    numberOfArithmeticSlices()