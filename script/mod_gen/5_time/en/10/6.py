def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort()
    i = 0
    j = 1
    count = 0
    while j < len(intervals):
        if intervals[i][1] > intervals[j][0]:
            count += 1
            if intervals[i][1] > intervals[j][1]:
                i = j
        else:
            i = j
        j += 1
    return count

if __name__ == '__main__':
    eraseOverlapIntervals()