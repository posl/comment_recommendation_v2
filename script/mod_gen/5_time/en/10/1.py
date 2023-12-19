def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1]]))
print(eraseOverlapIntervals([[1,2]]))
print(eraseOverlapIntervals([]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5],[-100,-2],[5,7],[-50,-1]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105],[106,107]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105],[106,107],[108,109]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-
