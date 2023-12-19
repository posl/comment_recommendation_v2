def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # DP
    # dp[i][j] = true if stone i can be reached by j steps
    # dp[i][j] = dp[k][j-1] or dp[k][j] or dp[k][j+1] where k < i and stones[i] - stones[k] = j
    # dp[0][0] = true
    # dp[1][1] = true
    # dp[2][1] = true
    # dp[2][2] = true
    # dp[3][2] = true
    # dp[3][3] = true
    # dp[3][4] = true
    # dp[4][3] = true
    # dp[4][4] = true
    # dp[4][5] = true
    # dp[5][4] = true
    # dp[5][5] = true
    # dp[5][6] = true
    # dp[6][5] = true
    # dp[6][6] = true
    # dp[6][7] = true
    # dp[7][6] = true
    # dp[7][7] = true
    # dp[7][8] = true
    # dp[8][7] = true
    # dp[8][8] = true
    # dp[8][9] = true
    # dp[9][8] = true
    # dp[9][9] = true
    # dp[9][10] = true
    # dp[10][9] = true
    # dp[10][10] = true
    # dp[10][11] = true
    # dp[11][10] = true
    # dp[11][11] = true
    # dp[11][12] = true
    # dp[12][11] = true
    # dp[12][12] = true
    # dp[12][13] = true
    # dp[13][12] = true
    # dp[13][13] = true
    # dp[13][14] = true
    # dp

if __name__ == '__main__':
    canCross()