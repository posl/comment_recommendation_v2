def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1] where j < i and stones[i] - stones[j] = k
    # dp[i][k] = False if stones[i] - stones[i-1] > k+1
    # dp[0][0] = True
    # dp[1][1] = True if stones[1] - stones[0] = 1
    # dp[i][k] = False for all other i and k
    # dp[n-1][k] = True for any k
    # return dp[n-1][k]
    n = len(stones)
    dp = [[False for _ in range(n)] for _ in range(n)]
    dp[0][0] = True
    for i in range(n):
        for j in range(i):
            k = stones[i] - stones[j]
            if k > j+1:
                continue
            dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
    return any(dp[n-1])

if __name__ == '__main__':
    canCross()