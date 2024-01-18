class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        pass

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = Solution()
    print(a.maxSumSubmatrix(matrix, k))