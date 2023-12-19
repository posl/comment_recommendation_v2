def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev = [1,1]
        for i in range(1,rowIndex):
            new = [1]
            for j in range(len(prev)-1):
                new.append(prev[j]+prev[j+1])
            new.append(1)
            prev = new
        return prev

if __name__ == '__main__':
    getRow()