class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_sum = float('-inf')
        for left in range(cols):
            row_sum = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    row_sum[row] += matrix[row][right]
                max_sum = max(max_sum, self.maxSumSubarray(row_sum, k))
        return max_sum

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))