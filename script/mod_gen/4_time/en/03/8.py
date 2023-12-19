def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # initialize the list with 1
    out = [1]
    # loop through the rowIndex
    for i in range(rowIndex):
        # initialize a temp list with 1
        temp = [1]
        # loop through the out list
        for j in range(len(out)-1):
            # append the sum of the current and next element
            temp.append(out[j] + out[j+1])
        # append the last 1
        temp.append(1)
        # update the out list
        out = temp
    # return the out list
    return out

if __name__ == '__main__':
    getRow()