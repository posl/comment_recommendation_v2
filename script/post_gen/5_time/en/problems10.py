Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[0])
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
            end = min(end, i[1])
    return count

=======
Suggestion 2

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1]]))
print(eraseOverlapIntervals([[1,2]]))
print(eraseOverlapIntervals([]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5],[-100,-2],[5,7],[-50,-1]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105],[106,107]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[-50,-1],[100,101],[102,103],[104,105],[106,107],[108,109]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-

=======
Suggestion 3

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key = lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count

=======
Suggestion 4

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[8,9],[10,11],[12,13],[14,15],[16,17],[18,19],[20,21]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-

=======
Suggestion 5

def eraseOverlapIntervals(intervals):
    intervals.sort()
    print(intervals)
    i = 0
    j = 1
    count = 0
    while j < len(intervals):
        if intervals[i][1] > intervals[j][0]:
            count += 1
            if intervals[i][1] > intervals[j][1]:
                i = j
            j += 1
        else:
            i = j
            j += 1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7],[5,7]]))
print(eraseOverlapInt

=======
Suggestion 6

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    count = 0
    end = -float('inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
        else:
            count += 1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[1,3],[2,3],[3,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8],[9,10]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8],[9,10],[10,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8],[9,10],[10,11],[11,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8],[9,10],[10,11],[11,12],[12,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[4,5],[6,8],[9,10],[10

=======
Suggestion 7

def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort()
    i = 0
    j = 1
    count = 0
    while j < len(intervals):
        if intervals[i][1] > intervals[j][0]:
            count += 1
            if intervals[i][1] > intervals[j][1]:
                i = j
        else:
            i = j
        j += 1
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

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))

=======
Suggestion 9

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) == 0:
        return 0
    intervals.sort(key = lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]
    return len(intervals) - count

=======
Suggestion 10

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
