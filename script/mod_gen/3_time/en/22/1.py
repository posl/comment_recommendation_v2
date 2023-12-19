def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid][1] < i[1]:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(i)
        else:
            dp[right] = i
    return len(dp)
print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print("The values above should be 3, 1, and 4.")

if __name__ == '__main__':
    maxEnvelopes()