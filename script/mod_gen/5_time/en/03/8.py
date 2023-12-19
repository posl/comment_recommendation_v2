def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    prev = [1,1]
    for i in range(1,rowIndex):
        current = [1]
        for j in range(0,len(prev)-1):
            current.append(prev[j]+prev[j+1])
        current.append(1)
        prev = current
    return current

if __name__ == '__main__':
    getRow()