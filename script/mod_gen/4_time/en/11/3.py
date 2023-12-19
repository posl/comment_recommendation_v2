def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==1: return 1
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

if __name__ == '__main__':
    lengthOfLIS()