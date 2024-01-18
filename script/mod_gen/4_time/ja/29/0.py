class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        return 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    a = Solution()
    print(a.longestIncreasingPath(matrix))