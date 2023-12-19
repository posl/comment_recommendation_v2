def twoSum(nums, target):
    """Return indices of the two numbers such that they add up to target.
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
    return 0

if __name__ == '__main__':
    twoSum()