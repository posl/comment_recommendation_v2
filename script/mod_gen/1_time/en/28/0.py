def maxSumSubmatrix(matrix, k):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    ans = float('-inf')
    for left in range(n):
        rowSum = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSum[i] += matrix[i][right]
            prefixSum = [0]
            cur = 0
            for r in rowSum:
                cur += r
                idx = bisect.bisect_left(prefixSum, cur - k)
                if idx < len(prefixSum):
                    ans = max(ans, cur - prefixSum[idx])
                bisect.insort(prefixSum, cur)
    return ans

if __name__ == '__main__':
    matrix = ==========please modify============
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)