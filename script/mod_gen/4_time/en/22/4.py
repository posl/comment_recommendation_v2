def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if envelopes[i][1] > dp[mid][1]:
                low = mid + 1
            else:
                high = mid - 1
        if low < len(dp):
            dp[low] = envelopes[i]
        else:
            dp.append(envelopes[i])
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print("The values above should be 3, 1, and 4.")

if __name__ == '__main__':
    maxEnvelopes()