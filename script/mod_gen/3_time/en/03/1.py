def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev_row = [1,1]
        for i in range(2,rowIndex+1):
            temp_row = [1]
            for j in range(1,len(prev_row)):
                temp_row.append(prev_row[j-1]+prev_row[j])
            temp_row.append(1)
            prev_row = temp_row
        return temp_row

if __name__ == '__main__':
    getRow()