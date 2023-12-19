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
