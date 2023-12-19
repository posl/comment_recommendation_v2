def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    n = len(intervals)
    if n < 2:
        return 0
    count = 1
    end = intervals[0][1]
    for i in range(1, n):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return n - count

if __name__ == '__main__':
    eraseOverlapIntervals()