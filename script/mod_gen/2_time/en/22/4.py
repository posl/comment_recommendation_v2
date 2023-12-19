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

if __name__ == '__main__':
    maxEnvelopes()