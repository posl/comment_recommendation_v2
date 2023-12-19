def pascalTriangle(numRows):
    #create empty list
    result = []
    #loop through the number of rows
    for i in range(numRows):
        #create an empty list
        row = []
        #loop through the range of i + 1
        for j in range(i + 1):
            #if j is equal to 0 or j is equal to i
            if j == 0 or j == i:
                #append 1 to row
                row.append(1)
            #else
            else:
                #append the sum of the previous row and the current row to row
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        #append row to result
        result.append(row)
    #return result
    return result

if __name__ == '__main__':
    pascalTriangle()