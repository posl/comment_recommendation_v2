class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float("-inf")
        for i in range(n):
            sums = [0] * m
            for j in range(i, n):
                for r in range(m):
                    sums[r] += matrix[r][j]
                res = max(res, self.maxSumSubarray(sums, k))
        return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))