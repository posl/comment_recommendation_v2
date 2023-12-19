def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))
print(maxEnvelopes([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print("The values above should be 3, 1, 3, 4, and 2.")

if __name__ == '__main__':
    maxEnvelopes()