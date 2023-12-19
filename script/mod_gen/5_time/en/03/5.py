def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex == 2:
        return [1,2,1]
    lst = [1,2,1]
    for i in range(2,rowIndex):
        lst.append(1)
        for j in range(i,0,-1):
            lst[j] = lst[j] + lst[j-1]
    return lst
print(getRow(3))
