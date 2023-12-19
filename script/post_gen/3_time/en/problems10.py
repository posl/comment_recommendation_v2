Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(intervals):
    intervals.sort()
    print(intervals)
    count = 0
    prev = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[prev][1]:
            count += 1
            if intervals[i][1] < intervals[prev][1]:
                prev = i
        else:
            prev = i
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]]))
print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9]]))

=======
Suggestion 2

def eraseOverlapIntervals(intervals):
    # Sort the intervals based on the end time
    intervals.sort(key=lambda x: x[1])
    # Keep track of the end time of the previous interval
    prev_end = intervals[0][1]
    # Keep track of the number of intervals that need to be removed
    count = 0
    # Iterate through the intervals
    for i in range(1, len(intervals)):
        # If the start time of the current interval is less than the end time of the previous interval
        if intervals[i][0] < prev_end:
            # Increment the count
            count += 1
        # Otherwise
        else:
            # Update the end time of the previous interval
            prev_end = intervals[i][1]
    # Return the count
    return count

=======
Suggestion 3

def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort(key = lambda x: x[1])
    end = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))

intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals))

=======
Suggestion 4

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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3],[6,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3],[6,8],[9,10]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3],[6,8],[9,10],[9,11]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3],[6,8],[9,10],[9,11],[10,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[5,6],[1,3],[6,8],[9,10],[9,11],[10,12],[11,13]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7

=======
Suggestion 5

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] < prev[1]:
            count += 1
        else:
            prev = curr
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[1,3],[2,3],[3,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8]]))

=======
Suggestion 6

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

=======
Suggestion 7

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
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
Suggestion 8

def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1])
    count = 0
    end = float('-inf')
    for i in intervals:
        if i[0] >= end:
            end = i[1]
            count += 1
    return len(intervals) - count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7]]))
print("The values above should be 1, 2, 0, 2, and 3.")

=======
Suggestion 9

def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort(key = lambda x: x[1])
    count = 1
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count

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
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[-100,-2],[5,7],[6,8],[7,9],[8,10],[9,11

=======
Suggestion 10

def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: x[1])
    #print(intervals)
    count = 0
    i = 0
    while i < len(intervals):
        j = i + 1
        while j < len(intervals):
            if intervals[i][1] > intervals[j][0]:
                count += 1
                del intervals[j]
            else:
                j += 1
        i += 1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7],[7,8]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6],[6,7],[7,8],[8,9]]))
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[2,4],[4,5],[4,6],[5,6
