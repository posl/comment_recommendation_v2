Synthesizing 10/10 solutions

=======
Suggestion 1

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    elif numRows == 3:
        return [[1], [1, 1], [1, 2, 1]]
    elif numRows == 4:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    elif numRows == 5:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    elif numRows == 6:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    elif numRows == 7:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1]]
    elif numRows == 8:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
    elif numRows == 9:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1,

=======
Suggestion 2

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
            pascal.append(row)
        return pascal

=======
Suggestion 3

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result

print(generate(5))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(6))
print(generate(7))
print(generate(8))
print(generate(9))
print(generate(10))
print(generate(11))
print(generate(12))
print(generate(13))
print(generate(14))
print(generate(15))
print(generate(16))
print(generate(17))
print(generate(18))
print(generate(19))
print(generate(20))
print(generate(21))
print(generate(22))
print(generate(23))
print(generate(24))
print(generate(25))
print(generate(26))
print(generate(27))
print(generate(28))
print(generate(29))
print(generate(30))

=======
Suggestion 4

def pascal_triangle(n):
    l = [[1]*i for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l

print(pascal_triangle(5))
print(pascal_triangle(1))
print(pascal_triangle(30))

=======
Suggestion 5

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

=======
Suggestion 6

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

=======
Suggestion 7

def generate(numRows):
    pascal = []
    for i in range(numRows):
        if i == 0:
            pascal.append([1])
        elif i == 1:
            pascal.append([1, 1])
        else:
            pascal.append([1])
            for j in range(len(pascal[i - 1]) - 1):
                pascal[i].append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            pascal[i].append(1)
    return pascal

=======
Suggestion 8

def generate(numRows):
    pascal = []
    for i in range(numRows):
        pascal.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i-1][j-1]+pascal[i-1][j])
    return pascal

print(generate(5))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(6))
print(generate(7))
print(generate(8))
print(generate(9))
print(generate(10))
print(generate(11))
print(generate(12))
print(generate(13))
print(generate(14))
print(generate(15))
print(generate(16))
print(generate(17))
print(generate(18))
print(generate(19))
print(generate(20))
print(generate(21))
print(generate(22))
print(generate(23))
print(generate(24))
print(generate(25))
print(generate(26))
print(generate(27))
print(generate(28))
print(generate(29))
print(generate(30))

=======
Suggestion 9

def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
    return pascal

print(generate(5))
print(generate(1))

=======
Suggestion 10

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
            result.append(temp)
        return result
