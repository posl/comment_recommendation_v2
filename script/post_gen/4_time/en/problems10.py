Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prevEnd = float('-inf')
    for i in intervals:
        if i[0] >= prevEnd:
            prevEnd = i[1]
        else:
            count += 1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print("The values above should be 1, 2, 0, 2, and 2.")

=======
Suggestion 2

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

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13]]))
print(eraseOverlapIntervals([[1,2],[2,3

=======
Suggestion 3

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
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
Suggestion 4

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals = sorted(intervals, key=lambda x: x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:
            count += 1
        else:
            prev = intervals[i]
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,100],[11,22],[1,11],[2,12]]
print(eraseOverlapIntervals(intervals))

=======
Suggestion 5

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) == 0:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            continue
        end = intervals[i][1]
        count += 1
    return len(intervals) - count


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,100],[11,22],[1,11],[2,12]]
print(eraseOverlapIntervals(intervals))
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3],[

=======
Suggestion 6

def eraseOverlapIntervals(intervals):
    intervals.sort()
    count = 0
    end = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] < end:
            count += 1
            end = min(intervals[i][1],end)
        else:
            end = intervals[i][1]
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11],[10,12],[11,13],[12,14]]))

=======
Suggestion 7

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key = lambda x:x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:
            count += 1
        else:
            prev = intervals[i]
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))
intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))

=======
Suggestion 8

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
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

=======
Suggestion 9

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) < 2:
        return 0

    intervals.sort(key=lambda x: x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:
            count += 1
        else:
            prev = intervals[i]
    return count

=======
Suggestion 10

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
