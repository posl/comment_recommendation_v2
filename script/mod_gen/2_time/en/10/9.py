def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev:
            count += 1
        else:
            prev = intervals[i][1]
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100],[101,102]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100],[101,102],[103,104]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100],[101,102],[103,104],[105,106]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100],[101,102],[103,104],[105,106],[107,108]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[-100,100],[101,102],[103,104],[105,106],[107,108],[109,110]]))
print(eraseOverlapIntervals([[1
