def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        list = [[1],[1,1]]
        for i in range(2, numRows):
            newList = [1]
            for j in range(1, i):
                newList.append(list[i-1][j-1] + list[i-1][j])
            newList.append(1)
            list.append(newList)
        return list
print(generate(5))
