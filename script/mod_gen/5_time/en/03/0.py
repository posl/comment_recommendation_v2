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
        res = [1,1]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(res[j-1]+res[j])
            temp.append(1)
            res = temp
        return res

if __name__ == '__main__':
    getRow()