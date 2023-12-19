def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,8,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10]))
