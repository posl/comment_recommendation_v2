def pascalTriangle(numRows):
    # initialize empty list
    triangle = []
    # loop through the number of rows
    for i in range(numRows):
        # initialize empty list
        row = []
        # loop through the number of columns
        for j in range(i+1):
            # if the first or last element, append 1
            if j == 0 or j == i:
                row.append(1)
            # else append the sum of the previous row
            # and the previous column
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # append the row to the triangle
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    pascalTriangle()