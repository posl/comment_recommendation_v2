def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        row = [1,1]
        for i in range(2,rowIndex+1):
            newRow = [1]
            for j in range(1,i):
                newRow.append(row[j-1]+row[j])
            newRow.append(1)
            row = newRow
        return row

if __name__ == '__main__':
    getRow()