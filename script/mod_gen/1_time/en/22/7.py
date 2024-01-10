def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = []
    for i in range(len(envelopes)):
        low, high = 0, len(dp) - 1
        while low <= high:
            mid = (low + high) // 2
            if dp[mid][1] < envelopes[i][1]:
                low = mid + 1
            else:
                high = mid - 1
        if low == len(dp):
            dp.append(envelopes[i])
        else:
            dp[low] = envelopes[i]
    return len(dp)

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = maxEnvelopes(envelopes)
    print(a)