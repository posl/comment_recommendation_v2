Synthesizing 10/10 solutions

=======
Suggestion 1

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if len(envelopes) == 0:
        return 0
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 2

def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

=======
Suggestion 3

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    tails = []
    for _, h in envelopes:
        l, r = 0, len(tails)
        while l < r:
            mid = (l + r) // 2
            if tails[mid] < h:
                l = mid + 1
            else:
                r = mid
        if r == len(tails):
            tails.append(h)
        else:
            tails[r] = h
    return len(tails)

=======
Suggestion 4

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    for i in range(len(envelopes)):
        dp[i] = 1
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))

=======
Suggestion 5

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

=======
Suggestion 6

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for _, h in envelopes:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if dp[m] < h:
                i = m + 1
            else:
                j = m
        dp[i] = h
        size = max(size, i + 1)
    return size

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))

=======
Suggestion 7

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for envelope in envelopes:
        idx = bisect.bisect_left(dp, envelope[1])
        if idx == len(dp):
            dp.append(envelope[1])
        else:
            dp[idx] = envelope[1]
    return len(dp)

=======
Suggestion 8

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for w, h in envelopes:
        l, r = 0, len(dp)
        while l < r:
            mid = (l + r) // 2
            if dp[mid][1] < h:
                l = mid + 1
            else:
                r = mid
        if r == len(dp):
            dp.append([w, h])
        else:
            dp[r][1] = h
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))

=======
Suggestion 9

def maxEnvelopes(envelopes):
    if not envelopes:
        return 0
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = [1]*len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

=======
Suggestion 10

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
