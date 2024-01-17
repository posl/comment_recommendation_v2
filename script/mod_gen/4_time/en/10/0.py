class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = Solution()
    print(a.eraseOverlapIntervals(intervals))