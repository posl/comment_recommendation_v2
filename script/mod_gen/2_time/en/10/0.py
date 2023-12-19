def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    end = -float('inf')
    count = 0
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[1,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[1,4],[2,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[1,4],[2,5],[3,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[1,4],[2,5],[3,5],[4,5]]))
