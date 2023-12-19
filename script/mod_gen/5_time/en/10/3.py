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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19],[20,21]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-
