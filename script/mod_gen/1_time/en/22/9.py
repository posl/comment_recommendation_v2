def maxEnvelopes(envelopes):
    if len(envelopes) == 0:
        return 0
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,1],[2,1],[3,1],[4,1]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4]]))
print(maxEnvelopes([[1,1],[2,3],[3,2],[4,4]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,4]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6],[5,1]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6],[5,1],[6,1]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6],[5,1],[6,1],[7,1]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6],[5,1],[6,1],[7,1],[8,1]]))
print(maxEnvelopes([[1,1],[2,3],[3,4],[4,5],[4,6],[5,1],[6,1],[7,1],[8,1],[9,1]]))
print(maxEnvelopes([[1,1],[2,3],[3,
