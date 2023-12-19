def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for envelope in envelopes:
        idx = bisect.bisect_left(dp, envelope[1])
        if idx == len(dp):
            dp.append(envelope[1])
        else:
            dp[idx] = envelope[1]
    return len(dp)

if __name__ == '__main__':
    maxEnvelopes()