def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i][j] = max coins from bursting all the balloons in nums[i:j+1]
    # dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]) for k in range(i,j+1)
    # dp[i][i] = nums[i-1]*nums[i]*nums[i+1]
    # dp[i][i+1] = max(dp[i][i] + dp[i+1][i+1] + nums[i-1]*nums[i]*nums[i+1],
    #                  dp[i][i] + dp[i+2][i+1] + nums[i-1]*nums[i+1]*nums[i+2])
    # dp[i][i+2] = max(dp[i][i+1] + dp[i+2][i+2] + nums[i-1]*nums[i]*nums[i+2],
    #                  dp[i][i+1] + dp[i+3][i+2] + nums[i-1]*nums[i+2]*nums[i+3],
    #                  dp[i][i] + dp[i+2][i+2] + nums[i-1]*nums[i]*nums[i+2],
    #                  dp[i][i] + dp[i+3][i+2] + nums[i-1]*nums[i+2]*nums[i+3])
    # dp[i][i+3] = max(dp[i][i+2] + dp[i+3][i+3] + nums[i-1]*nums[i]*nums[i+3],
    #                  dp[i][i+2] + dp[i+4][i+3] + nums[i-1]*nums[i+3]*nums[i+4],
    #                  dp[i][i+1] + dp[i+3][i+3] + nums[i-1]*nums[i]*nums[i+3],
    #                  dp[i][i+1] + dp[i+4][i+3] + nums[i-1]*nums[i+3]*nums[i+4])
    # dp[i][i+4] = max(dp[i][i+3] + dp[i+

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = maxCoins(nums)
    print(a)