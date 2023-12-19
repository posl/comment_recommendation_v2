def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        i = bisect.bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[1,3],[1,4],[1,5]]))
print(maxEnvelopes([[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]))
print(maxEnvelopes([[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]))
print("The values above should be 3, 1, 5, 5, and 7.")

if __name__ == '__main__':
    maxEnvelopes()