Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

=======
Suggestion 3

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

=======
Suggestion 4

def eraseOverlapIntervals(intervals):
    if len(intervals) < 2:
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

=======
Suggestion 5

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = -float('inf')
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    return count

=======
Suggestion 6

def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort(key=lambda x: x[0])
    count = 0
    curr = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[curr][1]:
            count += 1
            if intervals[i][1] < intervals[curr][1]:
                curr = i
        else:
            curr = i
    return count


print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))

=======
Suggestion 7

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key = lambda x: x[1])
    print(intervals)
    count = 0
    end = -float('inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

=======
Suggestion 8

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))

=======
Suggestion 9

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

=======
Suggestion 10

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
