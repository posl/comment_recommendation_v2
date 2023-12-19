def maxSumSubmatrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    maxSum = float('-inf')
    for left in range(cols):
        rowSum = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                rowSum[row] += matrix[row][right]
            maxSum = max(maxSum, maxSumSubArray(rowSum, k))
            if maxSum == k:
                return k
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()