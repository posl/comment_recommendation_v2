def eraseOverlapIntervals(intervals):
    if intervals == []:
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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3],[2,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3],[2,4],[3,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3],[2,4],[3,5],[4,6],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[1,3],[2,4],[3,5],[4,6],[5,7
