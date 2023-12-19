def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        prev_row = [1, 1]
        for i in range(2, rowIndex+1):
            curr_row = [1]
            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            curr_row.append(1)
            prev_row = curr_row
        return curr_row
print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
