Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
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
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))

=======
Suggestion 3

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    count = 0
    prev = 0
    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            if intervals[prev][1] > intervals[i][1]:
                prev = i
            count += 1
        else:
            prev = i
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

=======
Suggestion 4

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))

=======
Suggestion 5

def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    n = len(intervals)
    if n < 2:
        return 0
    count = 1
    end = intervals[0][1]
    for i in range(1, n):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return n - count

=======
Suggestion 6

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    erased = 0
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            erased += 1
    return erased

=======
Suggestion 7

def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

=======
Suggestion 8

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

=======
Suggestion 9

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
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

=======
Suggestion 10

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
