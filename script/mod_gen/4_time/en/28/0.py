def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    global_max = float('-inf')
    for i in range(len(matrix[0])):
        row_sum = [0 for _ in range(len(matrix))]
        for j in range(i, len(matrix[0])):
            for row in range(len(matrix)):
                row_sum[row] += matrix[row][j]
            global_max = max(global_max, kadane(row_sum, k))
    return global_max

if __name__ == '__main__':
    maxSumSubmatrix()