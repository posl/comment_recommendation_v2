Synthesizing 10/10 solutions

=======
Suggestion 1

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < h:
                left = mid + 1
            else:
                right = mid
        if right >= len(dp):
            dp.append(h)
        else:
            dp[right] = h
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))

=======
Suggestion 2

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for _, h in envelopes:
        l, r = 0, size
        while l < r:
            mid = (l + r) // 2
            if dp[mid] < h:
                l = mid + 1
            else:
                r = mid
        dp[l] = h
        size = max(size, l + 1)
    return size

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))

=======
Suggestion 3

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [0] * len(envelopes)
    size = 0
    for i in range(len(envelopes)):
        low, high = 0, size
        while low != high:
            mid = (low + high) // 2
            if dp[mid] < envelopes[i][1]:
                low = mid + 1
            else:
                high = mid
        dp[low] = envelopes[i][1]
        size = max(low + 1, size)
    return size

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8],[1,1]]))

=======
Suggestion 4

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # sort the array in ascending order by width, if width is equal, sort by height
    # then find the longest increasing subsequence of the height array
    # time complexity is O(nlogn) since sorting takes O(nlogn) and finding longest increasing subsequence takes O(nlogn)
    # space complexity is O(n) since we need an array to store the height
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    height = [e[1] for e in envelopes]
    return lengthOfLIS(height)

=======
Suggestion 5

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = []
    for _, h in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < h:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(h)
        else:
            dp[right] = h
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))
envelopes = [[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]
print(maxEnvelopes(envelopes))
envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]
print(maxEnvelopes(envelopes))
envelopes = [[17,15],[17,18],[2,8],[7,2],[17,2],[17,8],[3,11],[20,20],[17,20],[8,15],[3,15],[3,19],[8,9],[17,3],[6,14],[17,7],[17,14],[3,7],[20,8],[20,14],[20,17],[8,2],[20,6]]
print(maxEnvelopes(envelopes))
envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
print(maxEnvelopes(envelopes))
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print(maxEnvelopes(envelopes))
envelopes = [[30,50],[12,2],[3,4],[12,15]]
print(maxEnvelopes(envelopes))
envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = [1] * len(envelopes)
    for i in range(1, len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5],[6,6]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2],[2,2],[3,4],[4,4],[5,5],[6,6],[7,7]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,2

=======
Suggestion 9

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for w, h in envelopes:
        i = bisect.bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[2,1],[3,2],[4,3],[5,4],[6,5],[7,6]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[2,1],[3,2],[4,3],[5,4],[6,5],[7,6],[1,3],[2,4],[3,5],[4,6],[5,7]]))
print(maxEnvelopes([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[2,1],[3,2],[

=======
Suggestion 10

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]))
print(maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))
print(maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5],[10,6],[11,7],[12,8],[13,9],[14,10],[15,11]]))
print(maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5],[10,6],[11,7],[12,8],[13,9],[14,10],[15,11],[16,12],[17,13],[18,14],[19,15],[20,16],[21,17],[22,18],[23,19],[24,20],[25,21],[26,22],[27,23],[28,24],[29,25],[30,26],[31,27],[32,28],[33,29],[34,30],[35,31],[36,32],[37,33],[38,34],[39,35],[40,36],[41,37],[42,38],[43,39],[44,40],[45,41],[46,42],[47,43],[48,44],[49,45],[50,46],[51,47],[52,48],[53,49],[54,50],[55,51],[56,52],[57,53],[58,54],[59,55],[60,56],[61,57],[62
