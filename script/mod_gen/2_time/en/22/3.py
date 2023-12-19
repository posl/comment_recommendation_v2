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

if __name__ == '__main__':
    maxEnvelopes()