Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 空配列の場合は0を返す
        if len(intervals) == 0:
            return 0

        # 区間の終端でソートする
        intervals.sort(key=lambda x: x[1])

        # 最後に選んだ区間
        last = intervals[0]
        # 選んだ区間の数
        cnt = 1

        for i in range(1, len(intervals)):
            # 最後に選んだ区間と被る部分があるかどうか
            if intervals[i][0] < last[1]:
                continue

            # 区間が被っていなければ，区間を更新する
            last = intervals[i]
            cnt += 1

        # 区間を選ぶために削除する区間の数を返す
        return len(intervals) - cnt

=======
Suggestion 2

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = -float('inf')
        for s, e in intervals:
            if s < end:
                ans += 1
            else:
                end = e
        return ans

=======
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        pre = -float('inf')
        for start, end in intervals:
            if start < pre:
                ans += 1
            else:
                pre = end
        return ans

=======
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])
        ans = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        curr = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < curr:
                ans += 1
            else:
                curr = intervals[i][1]
        return ans

=======
Suggestion 6

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
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

=======
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort()
        ans = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]

        return ans

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
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
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        return count

=======
Suggestion 10

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = 1
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if right <= intervals[i][0]:
                ans += 1
                right = intervals[i][1]
        return len(intervals) - ans
