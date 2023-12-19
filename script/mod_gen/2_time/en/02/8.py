def pascalTriangle(numRows):
    pascal = []
    for i in range(numRows):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
        pascal.append(row)
    return pascal
print(pascalTriangle(5))
print(pascalTriangle(1))
print(pascalTriangle(10))
