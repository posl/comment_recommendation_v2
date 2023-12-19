def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    #print(matrix)
    #print(k)
    #print()
    if len(matrix) == 1 and len(matrix[0]) == 1:
        if matrix[0][0] <= k:
            return matrix[0][0]
        else:
            return -1
    elif len(matrix) == 1:
        for i in range(len(matrix[0])):
            matrix[0][i] += matrix[0][i-1]
        if max(matrix[0]) <= k:
            return max(matrix[0])
        else:
            return -1
    elif len(matrix[0]) == 1:
        for i in range(len(matrix)):
            matrix[i][0] += matrix[i-1][0]
        if max(matrix)[0] <= k:
            return max(matrix)[0]
        else:
            return -1
    else:
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        #print(matrix)
        #print()
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                matrix[i][j] += matrix[i-1][j]
        #print(matrix)
        #print()
        maxSum = -1000000
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for m in range(i, len(matrix)):
                    for n in range(j, len(matrix[0])):
                        if i == 0 and j == 0:
                            tempSum = matrix[m][n]
                        elif i == 0:
                            tempSum = matrix[m][n] - matrix[m][j-1]
                        elif j == 0:
                            tempSum = matrix[m][n] - matrix[i-1][n]
                        else:
                            tempSum = matrix[m][n] - matrix[i-1][n] - matrix[m][j-1] + matrix[i-1][j-1]
                        if tempSum <= k and tempSum > maxSum:
                            maxSum = tempSum
        if maxSum == -1000000:
            return -1
        else:
            return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()