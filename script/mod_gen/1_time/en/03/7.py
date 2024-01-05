def getRow(rowIndex):
    row = [1]
    for i in range(rowIndex):
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
    return row

if __name__ == '__main__':
    rowIndex = int(input())
    a = getRow(rowIndex)
    print(a)