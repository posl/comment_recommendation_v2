def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0:
                dp[i] = max(dp[i],dp[j]+1)
    maxIndex = dp.index(max(dp))
    res = [nums[maxIndex]]
    for i in range(maxIndex-1,-1,-1):
        if dp[i] == dp[maxIndex]-1 and nums[maxIndex]%nums[i] == 0:
            res.append(nums[i])
            maxIndex = i
    return res[::-1]
print(largestDivisibleSubset([1,2,3]))
print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([2,3,4,9,8]))
print(largestDivisibleSubset([1,2,3,4,5,6,7,8,9,10]))
