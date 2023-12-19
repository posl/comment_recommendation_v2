def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = [1]*len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

if __name__ == '__main__':
    maxEnvelopes()