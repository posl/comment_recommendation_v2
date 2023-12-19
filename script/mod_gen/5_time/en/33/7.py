def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            diff = nums[j] - nums[i]
            prev = nums[j]
            for k in range(j+1,len(nums)):
                if nums[k] - prev == diff:
                    count += 1
                    prev = nums[k]
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()