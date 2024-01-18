class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            sums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]
                res = max(res, self.helper(sums, k))
        return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))