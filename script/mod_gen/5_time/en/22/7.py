def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        idx = bisect.bisect_left(dp, envelopes[i][1])
        if idx == len(dp):
            dp.append(envelopes[i][1])
        else:
            dp[idx] = envelopes[i][1]
    return len(dp)

if __name__ == '__main__':
    maxEnvelopes()