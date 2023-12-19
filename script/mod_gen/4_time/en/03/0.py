def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
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
rowIndex = 3
print(getRow(rowIndex))
rowIndex = 0
print(getRow(rowIndex))
rowIndex = 1
print(getRow(rowIndex))
rowIndex = 2
print(getRow(rowIndex))
rowIndex = 33
print(getRow(rowIndex))
