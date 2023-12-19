def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = []
    for _,h in envelopes:
        i = bisect.bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print("The values above should be 3, 1, and 5.")

if __name__ == '__main__':
    maxEnvelopes()