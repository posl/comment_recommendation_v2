def pascalTriangle(numRows):
    triangle = []
    for i in range(numRows):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        if numRows != 0 and i != 0:
            triangle[i].append(1)
    return triangle
print(pascalTriangle(5))
