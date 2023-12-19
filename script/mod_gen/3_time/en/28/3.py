def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    max_sum = float('-inf')
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    max_sum = max(max_sum, sum(matrix[i][j:y+1]) + sum(matrix[x][j:y+1]))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()