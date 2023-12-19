def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    else:
        count = 0
        for i in range(0, len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

if __name__ == '__main__':
    numberOfArithmeticSlices()