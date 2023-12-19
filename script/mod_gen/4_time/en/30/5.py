def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    if stones[1] != 1:
        return False
    steps = {x: set() for x in stones}
    steps[1].add(1)
    for i in range(1, len(stones)):
        for j in steps[stones[i]]:
            for k in range(j-1, j+2):
                if k > 0 and stones[i]+k in steps:
                    steps[stones[i]+k].add(k)
    return len(steps[stones[-1]]) > 0

if __name__ == '__main__':
    canCross()