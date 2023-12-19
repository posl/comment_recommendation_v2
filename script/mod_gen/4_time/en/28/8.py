def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    max_sum = -float('inf')
    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    curr_sum = 0
                    for x in range(i, p+1):
                        for y in range(j, q+1):
                            curr_sum += matrix[x][y]
                    if curr_sum <= k:
                        if curr_sum > max_sum:
                            max_sum = curr_sum
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()