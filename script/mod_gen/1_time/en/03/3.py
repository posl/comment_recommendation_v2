def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        result = [1,1]
        for i in range(2, rowIndex+1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(result[j-1] + result[j])
            tmp.append(1)
            result = tmp
        return result

if __name__ == '__main__':
    getRow()