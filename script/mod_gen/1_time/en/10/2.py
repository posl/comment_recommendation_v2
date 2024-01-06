def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    count = 0
    if len(intervals) == 0:
        return count
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if prev[1] > curr[0]:
            count += 1
        else:
            prev = curr
    return count

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = eraseOverlapIntervals(intervals)
    print(a)