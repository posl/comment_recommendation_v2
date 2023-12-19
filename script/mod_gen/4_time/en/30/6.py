def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] > 1:
        return False
    dp = {}
    for s in stones:
        dp[s] = set()
    dp[0].add(1)
    for s in stones:
        for step in dp[s]:
            if s + step in dp:
                dp[s + step].add(step)
                dp[s + step].add(step + 1)
                if step - 1 > 0:
                    dp[s + step].add(step - 1)
    return len(dp[stones[-1]]) > 0
print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
print(canCross([0,2]))
print(canCross([0,1,3,6,10,15,16,21]))
print(canCross([0,1,3,6,9,10,13,15,18]))
print(canCross([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(canCross([0,1,3,4,5,7,9,10,12]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,27]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28]))
print(canCross([0,1,3,4,5,7,9,10,12,
