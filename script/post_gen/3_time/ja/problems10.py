Synthesizing 10/10 solutions

=======
Suggestion 1

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if last > intervals[i][0]:
                res += 1
            else:
                last = intervals[i][1]
        return res

=======
Suggestion 2

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = float('-inf')

        for i in intervals:
            if i[0] < end:
                ans += 1
            else:
                end = i[1]

        return ans

=======
Suggestion 3

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
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
Suggestion 4

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        end = -float('inf')
        for i in range(len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans

=======
Suggestion 5

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        #先に終了時間でソート
        intervals.sort(key=lambda x: x[1])
        #最初の終了時間を終了時間として記録
        end = intervals[0][1]
        #削除する必要がある区間数を記録
        count = 0
        #区間の数だけループ
        for i in range(1, len(intervals)):
            #前回の終了時間と今回の開始時間が重なっている場合
            if end > intervals[i][0]:
                #削除した区間数をインクリメント
                count += 1
            #重なっていない場合
            else:
                #終了時間を更新
                end = intervals[i][1]
        #削除した区間数を出力
        return count

=======
Suggestion 6

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 1.終了時間を基準にソート
        intervals.sort(key=lambda x:x[1])
        # 2.終了時間が早いものから順に取り除いていく
        ans = 0
        end = -float('inf')
        for s, e in intervals:
            if s < end:
                ans += 1
            else:
                end = e
        return ans

=======
Suggestion 7

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        #sort
        intervals.sort()
        #print(intervals)
        #check
        count = 0
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                count += 1
                if intervals[i][1] > intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
        return count

=======
Suggestion 8

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        end = -float('inf')
        for start, finish in intervals:
            if start < end:
                ans += 1
            else:
                end = finish
        return ans

=======
Suggestion 9

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
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

=======
Suggestion 10

def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
            else:
                end = intervals[i][1]
        return ans
