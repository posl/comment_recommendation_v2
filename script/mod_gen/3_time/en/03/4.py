def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    res = [1,1]
    for i in range(2,rowIndex+1):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(res[j-1]+res[j])
        res = temp
    return res
print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(4))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(8))
print(getRow(9))
