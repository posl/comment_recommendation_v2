def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    
    if rowIndex == 1:
        return [1,1]
    
    res = [1,1]
    for i in range(2, rowIndex+1):
        temp = [1]
        for j in range(1, len(res)):
            temp.append(res[j-1] + res[j])
        temp.append(1)
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
print(getRow(10))
print(getRow(11))
print(getRow(12))
print(getRow(13))
print(getRow(14))
print(getRow(15))
print(getRow(16))
print(getRow(17))
print(getRow(18))
print(getRow(19))
print(getRow(20))
print(getRow(21))
print(getRow(22))
print(getRow(23))
print(getRow(24))
print(getRow(25))
print(getRow(26))
print(getRow(27))
print(getRow(28))
print(getRow(29))
print(getRow(30))
print(getRow(31))
print(getRow(32))
print(getRow(33))
