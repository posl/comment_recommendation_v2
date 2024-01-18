Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        prev = float('-inf')
        for start, end in intervals:
            if start < prev:
                ans += 1
            else:
                prev = end
        return ans

=======
Suggestion 2

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        ans = 0
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
                end = min(intervals[i][1], end)
            else:
                start = intervals[i][0]
                end = intervals[i][1]
        return ans

=======
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans

=======
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                ans += 1
        return ans

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = -float('inf')
        for i in intervals:
            if i[0] < end:
                ans += 1
            else:
                end = i[1]
        return ans

=======
Suggestion 6

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1: return 0
        intervals.sort()
        ans = 0
        pre_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if pre_end > intervals[i][0]:
                ans += 1
                pre_end = min(pre_end, intervals[i][1])
            else:
                pre_end = intervals[i][1]
        return ans

=======
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        now = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if now > intervals[i][0]:
                ans += 1
            else:
                now = intervals[i][1]
        return ans

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        # 終了時間でソート
        intervals.sort(key=lambda x: x[1])
        # 一つ目は必ず残す
        prev_end = intervals[0][1]
        # 答え
        ans = 0
        for i in range(1, len(intervals)):
            # 開始時間が前の終了時間以降なら残す
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            # 開始時間が前の終了時間より前なら削除
            else:
                ans += 1
        return ans

=======
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        print(intervals)
        count = 0
        tmp = intervals[0]
        for interval in intervals[1:]:
            if tmp[1] > interval[0]:
                count += 1
                if tmp[1] > interval[1]:
                    tmp = interval
            else:
                tmp = interval
        return count
