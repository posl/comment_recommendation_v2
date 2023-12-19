def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    row = len(matrix)
    col = len(matrix[0])
    max_sum = -float('inf')
    for left in range(col):
        _sum = [0] * row
        for right in range(left, col):
            for i in range(row):
                _sum[i] += matrix[i][right]
            print(_sum)
            print("left: ", left, "right: ", right)
            print("max_sum: ", max_sum)
            print("k: ", k, "sum: ", _sum)
            print()
            max_sum = max(max_sum, maxSubArray(_sum, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()