def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = []
    for i in range(len(envelopes)):
        dp.append(1)
        for j in range(i):
            if envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return max(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))
print("The values above should be 3, 1, 5, and 3.")

if __name__ == '__main__':
    maxEnvelopes()