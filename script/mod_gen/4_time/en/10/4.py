def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            continue
        end = intervals[i][1]
        count += 1
    return len(intervals) - count
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,100],[11,22],[1,11],[2,12]]
print(eraseOverlapIntervals(intervals))
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[

if __name__ == '__main__':
    eraseOverlapIntervals()