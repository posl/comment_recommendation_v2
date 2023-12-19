def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        row = [1]
        last_row = getRow(rowIndex - 1)
        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i+1])
        row.append(1)
        return row
print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(33))
