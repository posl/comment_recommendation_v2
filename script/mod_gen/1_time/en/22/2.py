def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right - left) // 2
            if dp[mid] < h:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(h)
        else:
            dp[right] = h
    return len(dp)
        
#main function
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
