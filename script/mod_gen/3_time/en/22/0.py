def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key = lambda x: (x[0], -x[1]))
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
        size = max(i + 1, size)
    return size

if __name__ == '__main__':
    maxEnvelopes()