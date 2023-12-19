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
                    sub_matrix = matrix[i:(p+1)]
                    for idx, row in enumerate(sub_matrix):
                        sub_matrix[idx] = row[j:(q+1)]
                    sub_sum = sum([sum(row) for row in sub_matrix])
                    if sub_sum <= k and sub_sum > max_sum:
                        max_sum = sub_sum
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()