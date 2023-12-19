def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for i in range(1, rowIndex+1):
        row.append(int(row[i-1]*(rowIndex+1-i)/i))
    return row

if __name__ == '__main__':
    getRow()