def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = [[1],[1,1]]
    if numRows == 1:
        return result[0]
    if numRows == 2:
        return result
    for i in range(2,numRows):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j-1] + result[i-1][j])
        result.append(temp)
    return result
numRows = 5
print(generate(numRows))
