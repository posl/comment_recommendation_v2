def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for k in range(rowIndex):
        row.append(row[k] * (rowIndex-k) / (k+1))
    return row
print(getRow(3))
print(getRow(0))
print(getRow(1))
