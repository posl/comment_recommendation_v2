def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    result = float("-inf")
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            result = max(result, maxSumSubarray(sums, k))
            if result == k:
                return k
    return result

if __name__ == '__main__':
    maxSumSubmatrix()