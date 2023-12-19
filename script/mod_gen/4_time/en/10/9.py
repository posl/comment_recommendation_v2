def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count

if __name__ == '__main__':
    eraseOverlapIntervals()