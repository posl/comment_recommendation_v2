def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    #print(intervals)
    count = 0
    i = 0
    while i < len(intervals):
        j = i + 1
        while j < len(intervals):
            if intervals[i][1] > intervals[j][0]:
                count += 1
                del intervals[j]
            else:
                j += 1
        i += 1
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7],[7,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7],[7,8],[8,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6
