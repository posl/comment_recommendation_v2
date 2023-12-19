def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    #rowIndex is the number of row
    #rowIndex = 0 -> [1]
    #rowIndex = 1 -> [1,1]
    #rowIndex = 2 -> [1,2,1]
    #rowIndex = 3 -> [1,3,3,1]
    #rowIndex = 4 -> [1,4,6,4,1]
    
    #the number of col is equal to the number of row
    #so we can use rowIndex to determine the number of col
    
    #the first and last element of each row is 1
    #the middle elements are the sum of the elements in the previous row
    
    #create a list to store the elements of each row
    row = []
    
    #for rowIndex = 0, we just return [1]
    if rowIndex == 0:
        return [1]
    #for rowIndex = 1, we just return [1,1]
    elif rowIndex == 1:
        return [1,1]
    #for rowIndex = 2, we just return [1,2,1]
    elif rowIndex == 2:
        return [1,2,1]
    #for rowIndex = 3, we just return [1,3,3,1]
    elif rowIndex == 3:
        return [1,3,3,1]
    #for rowIndex = 4, we just return [1,4,6,4,1]
    elif rowIndex == 4:
        return [1,4,6,4,1]
    #for rowIndex > 4, we will use the formula to calculate the elements of each row
    else:
        #the first element of each row is 1
        row.append(1)
        #the number of elements in each row is equal to the number of row
        #so we use rowIndex to determine the number of elements in each row
        for i in range(1,rowIndex+1):
            #the middle elements are the sum of the elements in the previous row
            #so we use the formula to calculate the elements in the middle
            row.append(int(row[i-1]*(rowIndex-i+1)/i))
        #the last element of each row is 1

if __name__ == '__main__':
    getRow()