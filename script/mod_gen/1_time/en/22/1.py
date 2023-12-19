def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if len(envelopes) == 0:
        return 0
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1 for i in range(len(envelopes))]
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[5,6],[6,7],[7,8]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[5,5]]))
