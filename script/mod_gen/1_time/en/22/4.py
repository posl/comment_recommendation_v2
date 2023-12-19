def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        start, end = 0, len(dp)
        while start != end:
            mid = (start + end) // 2
            if dp[mid][1] < envelopes[i][1]:
                start = mid + 1
            else:
                end = mid
        if start == len(dp):
            dp.append(envelopes[i])
        else:
            dp[start] = envelopes[i]
    return len(dp)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
