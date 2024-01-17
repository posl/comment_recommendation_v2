class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                ans = max(ans, self.maxSumSubarray(total, k))
        return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))