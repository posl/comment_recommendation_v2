def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = maxEnvelopes(envelopes)
    print(a)