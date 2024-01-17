class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        max_sum = float('-inf')
        for i in range(len(matrix[0])):
            row_sum = [0] * len(matrix)
            for j in range(i, len(matrix[0])):
                for k in range(len(matrix)):
                    row_sum[k] += matrix[k][j]
                max_sum = max(max_sum, self.maxSumSubArray(row_sum, k))
        return max_sum

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))