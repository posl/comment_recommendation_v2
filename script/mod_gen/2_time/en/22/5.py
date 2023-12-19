def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        lo, hi = 0, len(dp)
        while lo < hi:
            mid = (lo + hi) // 2
            if dp[mid][1] < envelopes[i][1]:
                lo = mid + 1
            else:
                hi = mid
        if hi == len(dp):
            dp.append(envelopes[i])
        else:
            dp[hi] = envelopes[i]
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]))
print("The values above should be 3, 1, and 7.")

if __name__ == '__main__':
    maxEnvelopes()