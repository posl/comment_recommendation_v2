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
intervals = [[1,2],[2,3],[3,4],[1,3]]
result = eraseOverlapIntervals(intervals)
print(result)
intervals = [[1,2],[1,2],[1,2]]
result = eraseOverlapIntervals(intervals)
print(result)
intervals = [[1,2],[2,3]]
result = eraseOverlapIntervals(intervals)
print(result)

if __name__ == '__main__':
    eraseOverlapIntervals()