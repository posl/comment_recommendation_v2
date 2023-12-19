def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = None
    for left in range(cols):
        row_sums = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                row_sums[row] += matrix[row][right]
            max_sum = max(max_sum, maxSumSubarray(row_sums, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()