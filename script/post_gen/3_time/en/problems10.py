Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count

=======
Suggestion 2

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                count += 1
                end = min(end,intervals[i][1])
            else:
                end = intervals[i][1]
        return count

=======
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                count += 1
                intervals.pop(i+1)
            else:
                i += 1
        return count

=======
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                count += 1
            else:
                prev = intervals[i][1]
        return count

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
            else:
                count += 1
        return count

=======
Suggestion 6

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return len(intervals) - count

=======
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev = float('-inf')
        for interval in intervals:
            if interval[0] >= prev:
                prev = interval[1]
            else:
                count += 1
        return count

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        count = 0
        prev = float("-inf")
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                count += 1
        return count

=======
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
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
Suggestion 10

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        result = 0
        end = float('-inf')
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                result += 1
        return result
