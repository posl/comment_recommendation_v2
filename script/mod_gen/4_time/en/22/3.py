def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    for i in range(len(envelopes)):
        dp[i] = 1
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
