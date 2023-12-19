def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] < prev[1]:
            count += 1
        else:
            prev = curr
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[1,3],[2,3],[3,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]]))
