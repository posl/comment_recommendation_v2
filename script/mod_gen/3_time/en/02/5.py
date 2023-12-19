def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        pascal = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
            pascal.append(row)
    return pascal
print(pascal_triangle(5))
print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
