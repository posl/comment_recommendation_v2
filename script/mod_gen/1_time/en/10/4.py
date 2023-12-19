def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = -float('inf')
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    return count

if __name__ == '__main__':
    eraseOverlapIntervals()