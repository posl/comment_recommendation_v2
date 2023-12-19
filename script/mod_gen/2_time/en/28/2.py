def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        row_sums = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                row_sums[row] += matrix[row][right]
            max_sum = max(max_sum, max_sum_subarray(row_sums, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()