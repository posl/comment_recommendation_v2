def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    # Brute Force
    # Time Complexity: O((mn)^2)
    # Space Complexity: O(mn)
    # Time Limit Exceeded
    # m = len(matrix)
    # n = len(matrix[0])
    # max_sum = float('-inf')
    # for i in range(m):
    #     for j in range(n):
    #         for x in range(i, m):
    #             for y in range(j, n):
    #                 total = 0
    #                 for row in range(i, x + 1):
    #                     for col in range(j, y + 1):
    #                         total += matrix[row][col]
    #                 if total <= k:
    #                     max_sum = max(max_sum, total)
    # return max_sum
    
    # Time Complexity: O(mn^2)
    # Space Complexity: O(mn)
    # Time Limit Exceeded
    # m = len(matrix)
    # n = len(matrix[0])
    # max_sum = float('-inf')
    # for i in range(m):
    #     for j in range(1, n):
    #         matrix[i][j] += matrix[i][j - 1]
    # for i in range(n):
    #     for j in range(i, n):
    #         total = 0
    #         for x in range(m):
    #             if i > 0:
    #                 total += matrix[x][j] - matrix[x][i - 1]
    #             else:
    #                 total += matrix[x][j]
    #             if total <= k:
    #                 max_sum = max(max_sum, total)
    # return max_sum
    
    # Time Complexity: O(mn^2)
    # Space Complexity: O(mn)
    # Time Limit Exceeded
    # m = len(matrix)
    # n = len(matrix[0])
    # max_sum = float('-inf')
    # for i in range(m):
    #     for j in range(1, n):
    #         matrix[i][j] += matrix[i][j - 1]
    # for i in range(n):
    #     for j in

if __name__ == '__main__':
    maxSumSubmatrix()