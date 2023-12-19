def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    ans = -float('inf')
    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    curr = 0
                    for r in range(i, p+1):
                        for s in range(j, q+1):
                            curr += matrix[r][s]
                    if curr <= k:
                        ans = max(ans, curr)
    return ans

if __name__ == '__main__':
    maxSumSubmatrix()