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

if __name__ == '__main__':
    numberOfArithmeticSlices()