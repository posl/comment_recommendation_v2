def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    count = 0
    prev = 0
    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            if intervals[prev][1] > intervals[i][1]:
                prev = i
            count += 1
        else:
            prev = i
    return count

if __name__ == '__main__':
    eraseOverlapIntervals()