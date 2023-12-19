def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        low, high = 0, len(dp)
        while low < high:
            mid = (low + high) // 2
            if dp[mid][1] < envelopes[i][1]:
                low = mid + 1
            else:
                high = mid
        if high == len(dp):
            dp.append(envelopes[i])
        else:
            dp[high] = envelopes[i]
    return len(dp)

if __name__ == '__main__':
    maxEnvelopes()