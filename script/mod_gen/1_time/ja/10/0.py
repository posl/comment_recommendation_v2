class Solution:
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

if __name__ == '__main__':
    intervals = list(map(int, input().split()))
    intervals = [intervals[i:i+2] for i in range(0, len(intervals), 2)]
    a = Solution()
    print(a.eraseOverlapIntervals(intervals))