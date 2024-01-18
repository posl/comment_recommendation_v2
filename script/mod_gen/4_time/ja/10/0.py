class Solution:
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

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = Solution()
    print(a.eraseOverlapIntervals(intervals))