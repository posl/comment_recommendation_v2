Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        erase = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                erase += 1
            else:
                end = intervals[i][1]
        return erase

=======
Suggestion 2

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
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x[1])
        res = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                res += 1
                end = intervals[i][1]
        return len(intervals) - res

=======
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 区間の終点でソート
        intervals.sort(key=lambda x: x[1])
        # 区間の終点が重ならないようにするために削除する必要のある区間数の最小値
        erase_count = 0
        # 前回の区間の終点
        prev_end = float("-inf")
        for interval in intervals:
            # 前回の区間の終点と重なる場合
            if interval[0] < prev_end:
                erase_count += 1
            # 前回の区間の終点を更新
            else:
                prev_end = interval[1]
        return erase_count

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1
        
        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
                
        return n - ans

=======
Suggestion 6

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
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                cnt += 1
        return len(intervals) - cnt

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 区間の終端でソート
        intervals.sort(key=lambda x: x[1])
        # 区間の終端の最小値
        right = intervals[0][1]
        # 区間の数
        count = 1
        # 探索
        for interval in intervals[1:]:
            # 区間の終端が最小値以上の場合
            if interval[0] >= right:
                # 区間の数を増やす
                count += 1
                # 最小値を更新
                right = interval[1]
        # 削除する区間の数を出力
        return len(intervals) - count

=======
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = float('-inf')
        for s, e in intervals:
            if s < end:
                ans += 1
            else:
                end = e
        return ans
