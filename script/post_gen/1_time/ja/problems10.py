Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        ans = 0
        cur = float('-inf')
        for i in intervals:
            if i[0] >= cur:
                cur = i[1]
            else:
                ans += 1
        return ans

=======
Suggestion 2

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = -float('inf')
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                count += 1
        return count

=======
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans

=======
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        end = intervals[0][1]
        cnt = 1
        for i in range(1,len(intervals)):
            if intervals[i][0] >= end:
                cnt += 1
                end = intervals[i][1]
        return len(intervals) - cnt

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        count = 0
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                count += 1
        return count

=======
Suggestion 6

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 解答
        # 区間を終了時間でソートする
        intervals.sort(key=lambda x: x[1])
        # 区間の終了時間を比較するための変数
        end = -float("inf")
        # 重複している区間の数を数える変数
        count = 0
        # 区間を走査する
        for interval in intervals:
            # 現在の区間の開始時間が前の区間の終了時間よりも後ろであれば、重なっていない
            if interval[0] >= end:
                # 終了時間を更新する
                end = interval[1]
            # 現在の区間の開始時間が前の区間の終了時間よりも前であれば、重なっている
            else:
                # 重複している区間の数を増やす
                count += 1
        # 重複している区間の数を返す
        return count

=======
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 重なりを消すために消す区間の数を返す
        # 区間の終点でソートして貪欲法で解く
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = -float("inf")
        for s, e in intervals:
            if s < end:
                ans += 1
            else:
                end = e
        return ans

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        last_end = -float('inf')
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                ans += 1
        return ans

=======
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans

=======
Suggestion 10

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        ans = 0
        end = -float('inf')
        for s, e in intervals:
            if s >= end:
                end = e
            else:
                ans += 1
        return ans
