def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n^2) solution
    # dp = [1] * len(nums)
    # for i in range(len(nums)):
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # return max(dp)
    
    # O(n log n) solution
    dp = []
    for num in nums:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    return len(dp)

if __name__ == '__main__':
    lengthOfLIS()