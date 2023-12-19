def getRow(rowIndex):
    #create list of zeros
    result = [0] * (rowIndex + 1)
    #set first element to 1
    result[0] = 1
    #loop through rowIndex
    for i in range(rowIndex + 1):
        #loop through row backwards
        for j in range(i, 0, -1):
            #add current value to previous value
            result[j] = result[j] + result[j - 1]
    #return result
    return result

if __name__ == '__main__':
    getRow()