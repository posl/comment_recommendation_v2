def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) < 2:
        return nums
    nums.sort()
    res = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]
    return max(res, key=len)
print(largestDivisibleSubset([1,2,4,8]))
