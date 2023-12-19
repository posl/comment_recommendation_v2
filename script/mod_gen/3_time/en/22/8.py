def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for w, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid][1] < h:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append([w, h])
        else:
            dp[right] = [w, h]
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
