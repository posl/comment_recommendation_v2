def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], sum(nums[l:j])))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j-1]))
    #dp[i][j] = min(dp[i][j], max(dp[i-1][l], dp[l+1][j]))
    #dp[i][

if __name__ == '__main__':
    splitArray()