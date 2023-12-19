def eraseOverlapIntervals(intervals):
    intervals.sort()
    print(intervals)
    count = 0
    prev = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[prev][1]:
            count += 1
            if intervals[i][1] < intervals[prev][1]:
                prev = i
        else:
            prev = i
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9]]))
