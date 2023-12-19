def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
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