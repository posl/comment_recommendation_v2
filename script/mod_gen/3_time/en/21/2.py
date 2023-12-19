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

if __name__ == '__main__':
    numberOfArithmeticSlices()