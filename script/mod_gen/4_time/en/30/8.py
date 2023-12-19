def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return True if stones[2] == 2 else False
    dp = {}
    for stone in stones:
        dp[stone] = set()
    dp[0].add(1)
    for stone in stones[:-1]:
        for step in dp[stone]:
            if stone + step == stones[-1]:
                return True
            if stone + step in dp:
                dp[stone + step].add(step)
                dp[stone + step].add(step + 1)
                dp[stone + step].add(step - 1)
    return False

if __name__ == '__main__':
    canCross()