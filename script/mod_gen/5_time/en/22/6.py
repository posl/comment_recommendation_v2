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

if __name__ == '__main__':
    maxEnvelopes()