def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    else:
        return [1] + [sum(x) for x in zip(getRow(rowIndex-1), getRow(rowIndex-1)[1:])] + [1]
    
#Test Case
rowIndex = 4
print(getRow(rowIndex))
