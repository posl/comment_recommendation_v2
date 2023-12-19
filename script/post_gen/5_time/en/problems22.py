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
        if right == len(dp):
            dp.append(h)
        else:
            dp[right] = h
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))

envelopes = [[1,1],[1,1],[1,1]]
print(maxEnvelopes(envelopes))

envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
print(maxEnvelopes(envelopes))

=======
Suggestion 2

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
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

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[30,50],[12,2],[3,4],[12,15]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46],[46,89],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46]]))
print(maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46],[50,53],[52,68],[72,45],[77,81],[81,77],[89,46],[46,89],[50,53

=======
Suggestion 3

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for _, h in envelopes:
        i = bisect.bisect_left(dp, h)
        if i == len(dp):
            dp.append(h)
        else:
            dp[i] = h
    return len(dp)

=======
Suggestion 4

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print("The values above should be 3, 1, and 4.")

=======
Suggestion 5

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(maxEnvelopes([[1,1],[1,1],[1,1]]))
print(maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
print(maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))
print(maxEnvelopes([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print("The values above should be 3, 1, 3, 4, and 2.")

=======
Suggestion 6

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if len(envelopes) == 0:
        return 0
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1]
    for i in range(1, len(envelopes)):
        dp.append(1)
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

=======
Suggestion 7

def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    #sort envelopes by width
    envelopes.sort(key=lambda x: x[0])
    #create dp array
    dp = [1 for i in range(len(envelopes))]
    #iterate through envelopes
    for i in range(len(envelopes)):
        #iterate through all previous envelopes
        for j in range(i):
            #if current envelope can fit into previous envelope
            if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                #update dp array
                dp[i] = max(dp[i], dp[j] + 1)
    #return max of dp array
    return max(dp)

=======
Suggestion 8

def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = []
    for i in range(len(envelopes)):
        idx = bisect.bisect_left(dp, envelopes[i][1])
        if idx == len(dp):
            dp.append(envelopes[i][1])
        else:
            dp[idx] = envelopes[i][1]
    return len(dp)

=======
Suggestion 9

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

=======
Suggestion 10

def maxEnvelopes(envelopes):
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    dp = []
    for env in envelopes:
        left, right = 0, len(dp)
        while left < right:
            mid = left + (right - left) // 2
            if dp[mid][1] < env[1]:
                left = mid + 1
            else:
                right = mid
        if right == len(dp):
            dp.append(env)
        else:
            dp[right] = env
    return len(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(envelopes))
