def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: x[0])
    dp = [1] * len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
