class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -10**5
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        total = 0
                        for x in range(i, p+1):
                            for y in range(j, q+1):
                                total += matrix[x][y]
                        if total <= k:
                            ans = max(ans, total)
        return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))