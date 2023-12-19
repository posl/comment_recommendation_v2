def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    else:
        result = [1,1]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(result[j-1]+result[j])
            temp.append(1)
            result = temp
        return result
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
print(getRow(5))
