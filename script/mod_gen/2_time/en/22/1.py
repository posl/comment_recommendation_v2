def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for _, h in envelopes:
        l, r = 0, size
        while l < r:
            mid = (l + r) // 2
            if dp[mid] < h:
                l = mid + 1
            else:
                r = mid
        dp[l] = h
        size = max(size, l + 1)
    return size
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
