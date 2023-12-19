def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    result = [[1]]
    for i in range(1, rowIndex + 1):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)
    return result[rowIndex]
print(getRow(3))
print(getRow(0))
print(getRow(1))
