def eraseOverlapIntervals(intervals):
    intervals.sort()
    count = 0
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] < end:
            count += 1
            end = min(intervals[i][1],end)
        else:
            end = intervals[i][1]
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14]]))
