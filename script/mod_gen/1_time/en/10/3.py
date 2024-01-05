def eraseOverlapIntervals(intervals):
    if len(intervals) < 2:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count

if __name__ == '__main__':
    intervals = ==========please modify============
    a = eraseOverlapIntervals(intervals)
    print(a)