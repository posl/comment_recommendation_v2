def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) < 2:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:
            count += 1
        else:
            prev = intervals[i]
    return count

if __name__ == '__main__':
    eraseOverlapIntervals()