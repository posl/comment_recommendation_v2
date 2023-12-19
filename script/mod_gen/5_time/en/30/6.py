def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # 1 <= stones.length <= 2000
    # 0 <= stones[i] <= 2^31 - 1
    # stones[0] == 0
    # stones is sorted in a strictly increasing order.
    # 1st approach: DP
    # dp[i][j] = True if we can reach stone i with jump j
    #           False otherwise
    # dp[0][0] = True
    # dp[i][j] = dp[i-j][j-1] or dp[i-j][j] or dp[i-j][j+1]
    #           where 1 <= j <= i
    #           and i-j >= 0
    #           and i-j <= i-1
    #           and i-j+1 <= i
    #           and i-j+1 >= 1
    #           and stones[i] - stones[i-j] <= i
    #           and stones[i] - stones[i-j] >= 1
    #           and stones[i] - stones[i-j+1] <= i-1
    #           and stones[i] - stones[i-j+1] >= 0
    #           and stones[i] - stones[i-j-1] <= i+1
    #           and stones[i] - stones[i-j-1] >= -1
    #           and stones[i] - stones[i-j+1] == j
    #           and stones[i] - stones[i-j] == j
    #           and stones[i] - stones[i-j-1] == j
    #           and stones[i] - stones[i-j+1] == j
    #           and stones[i] - stones[i-j] == j+1
    #           and stones[i] - stones[i-j-1] == j+1
    #           and stones[i] - stones[i-j+1] == j+1
    #           and stones[i] - stones[i-j] == j-1
    #           and stones[i] - stones[i-j-1] == j-1
    #           and stones[i] - stones[i-j+1] == j-1
    #           and stones[i] - stones[i-j] == j

if __name__ == '__main__':
    canCross()