def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    result = []
    for i in range(rowIndex+1):
        result.append(1)
        for j in range(i-1, 0, -1):
            result[j] += result[j-1]
    return result

if __name__ == '__main__':
    getRow()