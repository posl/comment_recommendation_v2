def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    row = [1,1]
    for i in range(2,rowIndex+1):
        temp = [1]
        for j in range(1,i):
            temp.append(row[j-1]+row[j])
        temp.append(1)
        row = temp
    return row
print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(33))
