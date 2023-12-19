def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # sort the envelopes by width and then by height
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    # create an array to store the longest increasing subsequence
    dp = [0]*len(envelopes)
    # initialize the length of the longest increasing subsequence
    length = 0
    # iterate through the envelopes
    for envelope in envelopes:
        # initialize the indices for binary search
        low, high = 0, length
        # perform binary search to find the index where the envelope should be placed
        while low < high:
            mid = (low + high) // 2
            if dp[mid] < envelope[1]:
                low = mid + 1
            else:
                high = mid
        # store the envelope at the index returned by binary search
        dp[low] = envelope[1]
        # if the index returned by binary search is equal to the length of the longest increasing subsequence
        if low == length:
            # increment the length of the longest increasing subsequence
            length += 1
    # return the length of the longest increasing subsequence
    return length

if __name__ == '__main__':
    maxEnvelopes()