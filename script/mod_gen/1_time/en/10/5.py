def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort(key=lambda x: x[0])
    count = 0
    curr = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[curr][1]:
            count += 1
            if intervals[i][1] < intervals[curr][1]:
                curr = i
        else:
            curr = i
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
