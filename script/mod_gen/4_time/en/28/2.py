def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    result = float("-inf")
    for left in range(cols):
        rowSum = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                rowSum[i] += matrix[i][right]
            result = max(result, maxSumSubArray(rowSum, k))
            if result == k:
                return k
    return result

if __name__ == '__main__':
    maxSumSubmatrix()