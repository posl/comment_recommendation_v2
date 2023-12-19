def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for _, h in envelopes:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if dp[m] < h:
                i = m + 1
            else:
                j = m
        dp[i] = h
        size = max(size, i + 1)
    return size
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
