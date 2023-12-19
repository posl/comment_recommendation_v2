def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for w, h in envelopes:
        l, r = 0, len(dp)
        while l < r:
            mid = (l + r) // 2
            if dp[mid][1] < h:
                l = mid + 1
            else:
                r = mid
        if r == len(dp):
            dp.append([w, h])
        else:
            dp[r][1] = h
    return len(dp)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))
