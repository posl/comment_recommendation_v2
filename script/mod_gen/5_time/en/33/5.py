def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(1, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] - nums[i] == nums[i] - nums[i - 1]:
                count += 1
            else:
                break
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()