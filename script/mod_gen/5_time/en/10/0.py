class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                count += 1
            else:
                prev = intervals[i]
        return count

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = Solution()
    print(a.eraseOverlapIntervals(intervals))