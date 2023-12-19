def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    n = len(stones)
    if stones[1] != 1:
        return False
    dp = [[False for _ in range(n)] for _ in range(n)]
    dp[1][1] = True
    for i in range(2, n):
        for j in range(1, i):
            diff = stones[i] - stones[j]
            if diff < 0 or diff > n or not dp[j][diff]:
                continue
            dp[i][diff] = True
            if diff - 1 >= 0:
                dp[i][diff - 1] = True
            if diff + 1 <= n:
                dp[i][diff + 1] = True
            if i == n - 1:
                return True
    return False
stones = [0,1,3,5,6,8,12,17]
print(canCross(stones))
