def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key = lambda x:x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:
            count += 1
        else:
            prev = intervals[i]
    return count
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
