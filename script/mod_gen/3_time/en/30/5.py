def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    dp = {}
    for i in stones:
        dp[i] = set()
    dp[0].add(0)
    for i in stones:
        for j in dp[i]:
            for k in range(j - 1, j + 2):
                if k > 0 and i + k in dp:
                    dp[i + k].add(k)
    return len(dp[stones[-1]]) > 0

if __name__ == '__main__':
    canCross()