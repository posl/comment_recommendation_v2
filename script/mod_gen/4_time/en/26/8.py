def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # O(n^2)
    # dp[i][j] is the minimum largest sum of splitting nums[0] ~ nums[i] into j parts
    # dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1]))) for k in range(i)
    # ans = dp[-1][-1]
    # dp = [[float('inf')] * (m+1) for _ in range(len(nums))]
    # dp[0][1] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i][1] = dp[i-1][1] + nums[i]
    # for i in range(1, len(nums)):
    #     for j in range(2, min(i+2, m+1)):
    #         for k in range(i):
    #             dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1])))
    # return dp[-1][-1]
    # O(nlog(sum))
    # dp[i][j] is the minimum largest sum of splitting nums[0] ~ nums[i] into j parts
    # dp[i][j] = min(dp[i][j], max(dp[k][j-1], sum(nums[k+1:i+1]))) for k in range(i)
    # ans = dp[-1][-1]
    # dp = [[float('inf')] * (m+1) for _ in range(len(nums))]
    # dp[0][1] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i][1] = dp[i-1][1] + nums[i]
    # for i in range(1, len(nums)):
    #     for j in range(2, min(i+2, m+1)):
    #         l, r = 0, i
    #         while l < r:
    #             mid = (l+r) // 2
    #             if dp[mid][j-1] > sum(nums[mid+1:i+1]):
    #                 r = mid
    #

if __name__ == '__main__':
    splitArray()