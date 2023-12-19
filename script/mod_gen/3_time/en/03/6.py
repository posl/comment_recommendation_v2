def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    #create a list of lists
    pascal = [[1]*(i+1) for i in range(rowIndex+1)]
    for i in range(rowIndex+1):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal[rowIndex]
    
#Time complexity: O(n^2)
#Space complexity: O(n^2)

if __name__ == '__main__':
    getRow()