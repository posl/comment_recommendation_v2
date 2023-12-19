def pascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        pascal = [[1], [1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
            pascal.append(row)
        return pascal
print(pascalTriangle(5))
print(pascalTriangle(1))
print(pascalTriangle(2))
print(pascalTriangle(3))
print(pascalTriangle(4))
print(pascalTriangle(6))
print(pascalTriangle(7))
print(pascalTriangle(8))
print(pascalTriangle(9))
print(pascalTriangle(10))
print(pascalTriangle(11))
print(pascalTriangle(12))
print(pascalTriangle(13))
print(pascalTriangle(14))
print(pascalTriangle(15))
print(pascalTriangle(16))
print(pascalTriangle(17))
print(pascalTriangle(18))
print(pascalTriangle(19))
print(pascalTriangle(20))
print(pascalTriangle(21))
print(pascalTriangle(22))
print(pascalTriangle(23))
print(pascalTriangle(24))
print(pascalTriangle(25))
print(pascalTriangle(26))
print(pascalTriangle(27))
print(pascalTriangle(28))
print(pascalTriangle(29))
print(pascalTriangle(30))
