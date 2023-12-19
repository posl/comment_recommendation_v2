def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    prev_row = [1,1]
    for i in range(2,rowIndex+1):
        curr_row = [1]
        for j in range(1,i):
            curr_row.append(prev_row[j-1]+prev_row[j])
        curr_row.append(1)
        prev_row = curr_row
    return curr_row

if __name__ == '__main__':
    getRow()