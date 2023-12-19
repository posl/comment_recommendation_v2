def lengthOfLIS(nums):
    dp = [1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

if __name__ == '__main__':
    lengthOfLIS()