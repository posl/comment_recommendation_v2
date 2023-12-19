Synthesizing 10/10 solutions

=======
Suggestion 1

def generate(numRows):
    pascal = []
    for i in range(numRows):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row)-1):
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]
        pascal.append(row)
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
Suggestion 2

def generate(numRows):
    result = []
    for i in range(numRows):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row)-1):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

print(generate(5))
print(generate(1))

=======
Suggestion 3

def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            result.append([1] * (i + 1))
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result

=======
Suggestion 4

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
Suggestion 5

def pascalTriangle(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1], [1, 1]]
    if numRows > 2:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            result.append([1])
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
    return result

print(pascalTriangle(5))
print(pascalTriangle(1))
print(pascalTriangle(0))
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

=======
Suggestion 6

def pascalTriangle(numRows):
    triangle = []
    for row in range(numRows):
        triangle.append([])
        triangle[row].append(1)
        for col in range(1, row):
            triangle[row].append(triangle[row-1][col-1] + triangle[row-1][col])
        if row != 0:
            triangle[row].append(1)
    return triangle

print(pascalTriangle(5))
print(pascalTriangle(1))

=======
Suggestion 7

def pascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(result[i-1][j-1] + result[i-1][j])
            temp.append(1)
            result.append(temp)
        return result

=======
Suggestion 8

def generate(numRows):
    triangle = []

    for row_num in range(numRows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

=======
Suggestion 9

def pascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    elif numRows > 2:
        triangle = [[1],[1,1]]
        for i in range(2,numRows):
            row = [1]
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

print(pascalTriangle(1))
print(pascalTriangle(2))
print(pascalTriangle(3))
print(pascalTriangle(4))
print(pascalTriangle(5))
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

=======
Suggestion 10

def pascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        triangle = [[1],[1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

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
