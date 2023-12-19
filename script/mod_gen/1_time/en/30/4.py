def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return True
    
    if stones[1] != 1:
        return False
    
    if len(stones) == 2:
        return True
    
    dp = {}
    for i in range(len(stones)):
        dp[stones[i]] = set()
    dp[stones[1]].add(1)
    
    for i in range(len(stones)):
        for k in dp[stones[i]]:
            if stones[i] + k - 1 in dp:
                dp[stones[i] + k - 1].add(k - 1)
            if stones[i] + k in dp:
                dp[stones[i] + k].add(k)
            if stones[i] + k + 1 in dp:
                dp[stones[i] + k + 1].add(k + 1)
    
    return len(dp[stones[-1]]) > 0
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
print(canCross([0,2]))
