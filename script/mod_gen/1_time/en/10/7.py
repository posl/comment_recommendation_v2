def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
