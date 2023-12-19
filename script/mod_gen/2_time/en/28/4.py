def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m=len(matrix)
    n=len(matrix[0])
    maxSum=-1000000
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                matrix[i][j]=matrix[i][j]
            elif i==0:
                matrix[i][j]=matrix[i][j]+matrix[i][j-1]
            elif j==0:
                matrix[i][j]=matrix[i][j]+matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i][j]+matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
    for i in range(m):
        for j in range(n):
            for p in range(i,m):
                for q in range(j,n):
                    if i==0 and j==0:
                        sum=matrix[p][q]
                    elif i==0:
                        sum=matrix[p][q]-matrix[p][j-1]
                    elif j==0:
                        sum=matrix[p][q]-matrix[i-1][q]
                    else:
                        sum=matrix[p][q]-matrix[p][j-1]-matrix[i-1][q]+matrix[i-1][j-1]
                    if sum<=k:
                        maxSum=max(maxSum,sum)
    return maxSum
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix,k))
matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix,k))
