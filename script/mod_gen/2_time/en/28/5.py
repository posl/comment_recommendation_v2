def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    result = float("-inf")
    for left in range(n):
        sums = [0] * m
        for right in range(left, n):
            for i in range(m):
                sums[i] += matrix[i][right]
            result = max(result, maxSumSubArray(sums, k))
    return result

if __name__ == '__main__':
    maxSumSubmatrix()