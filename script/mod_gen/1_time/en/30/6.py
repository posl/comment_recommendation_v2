def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    n = len(stones)
    if n == 2:
        return True
    dp = [[False for i in range(n)] for j in range(n)]
    dp[1][1] = True
    for i in range(2, n):
        for j in range(1, i):
            k = stones[i] - stones[j]
            if k <= j + 1:
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True
    return False

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = canCross(stones)
    print(a)