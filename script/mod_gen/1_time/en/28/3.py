def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    ans = float('-inf')
    for left in range(col):
        rowSum = [0] * row
        for right in range(left, col):
            for i in range(row):
                rowSum[i] += matrix[i][right]
            ans = max(ans, maxSumSubarray(rowSum, k))
            if ans == k:
                return k
    return ans

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)