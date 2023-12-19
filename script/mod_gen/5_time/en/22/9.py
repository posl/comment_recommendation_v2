def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = []
    for env in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right - left) // 2
            if dp[mid][1] < env[1]:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(env)
        else:
            dp[right] = env
    return len(dp)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
