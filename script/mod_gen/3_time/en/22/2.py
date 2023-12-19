def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid][1] < envelopes[i][1]:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(envelopes[i])
        else:
            dp[right] = envelopes[i]
    return len(dp)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print(maxEnvelopes(envelopes))
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,2]]
print(maxEnvelopes(envelopes))
envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
print(maxEnvelopes(envelopes))
