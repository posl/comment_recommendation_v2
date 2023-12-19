def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = [1] * len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5],[6,6]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5],[6,6],[7,7]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2
