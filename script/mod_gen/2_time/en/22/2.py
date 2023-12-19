def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for i in range(len(envelopes)):
        low, high = 0, size
        while low != high:
            mid = (low + high) // 2
            if dp[mid] < envelopes[i][1]:
                low = mid + 1
            else:
                high = mid
        dp[low] = envelopes[i][1]
        size = max(low + 1, size)
    return size
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8],[1,1]]))
