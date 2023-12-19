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

if __name__ == '__main__':
    numberOfArithmeticSlices()