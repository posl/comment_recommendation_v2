def maxSumSubmatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    res = float('-inf')
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            res = max(res, maxSumSubarray(sums, k))
            if res == k:
                return k
    return res

if __name__ == '__main__':
    maxSumSubmatrix()