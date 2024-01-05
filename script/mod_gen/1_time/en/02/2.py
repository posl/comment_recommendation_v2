def generate(numRows):
    #create a variable to store the list
    triangle = []
    #loop through the range of the number of rows
    for row_num in range(numRows):
        #create a row list to store the values for each row
        row = []
        #loop through the range of the row number
        for col_num in range(row_num+1):
            #if the column number is 0 or the column number is equal to the row number
            if col_num == 0 or col_num == row_num:
                #append 1 to the row list
                row.append(1)
            else:
                #if not, append the value of the row above and the column number -1 and the value of the row above and the column number
                row.append(triangle[row_num-1][col_num-1] + triangle[row_num-1][col_num])
        #append the row list to the triangle list
        triangle.append(row)
    #return the triangle list
    return triangle

if __name__ == '__main__':
    numRows = int(input())
    a = generate(numRows)
    print(a)