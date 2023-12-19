def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    erased = 0
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            erased += 1
    return erased

if __name__ == '__main__':
    eraseOverlapIntervals()