def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda a: a[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] < prev[1]:
            count += 1
        else:
            prev = curr
    return count

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = eraseOverlapIntervals(intervals)
    print(a)