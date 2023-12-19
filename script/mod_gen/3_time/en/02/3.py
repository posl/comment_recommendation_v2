def pascal_triangle(n):
    l = [[1]*i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l
print(pascal_triangle(5))
print(pascal_triangle(1))
print(pascal_triangle(30))
