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
        sums = [0] * n
        for j in range(i, m):
            for col in range(n):
                sums[col] += matrix[j][col]
            max_sum = max(max_sum, maxSubArray(sums, k))
            if max_sum == k:
                return k
    return max_sum

if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)