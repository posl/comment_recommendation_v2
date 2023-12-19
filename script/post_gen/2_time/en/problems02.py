Synthesizing 10/10 solutions

=======
Suggestion 1

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
        return [[1],[1,1]]
    elif numRows > 2:
        result = [[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for j in range(1,i):
                temp.append(result[i-1][j-1]+result[i-1][j])
            temp.append(1)
            result.append(temp)
        return result

numRows = 5
print(generate(numRows))

=======
Suggestion 3

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

=======
Suggestion 4

def generate(numRows):
    pascal = []
    for i in range(numRows):
        pascal.append([])
        pascal[i].append(1)
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        if(numRows != 0 and i != 0):
            pascal[i].append(1)
    return pascal

print(generate(5))
print(generate(1))
print(generate(0))

=======
Suggestion 5

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        result = [[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for j in range(1,i):
                temp.append(result[i-1][j-1]+result[i-1][j])
            temp.append(1)
            result.append(temp)
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
Suggestion 6

def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        triangle = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1]
            for j in range(1,i-1):
                temp.append(triangle[i-2][j-1]+triangle[i-2][j])
            temp.append(1)
            triangle.append(temp)
        return triangle

=======
Suggestion 7

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    result = [[1],[1,1]]
    if numRows == 1:
        return result[0]
    if numRows == 2:
        return result
    for i in range(2,numRows):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j-1] + result[i-1][j])
        result.append(temp)
    return result

numRows = 5
print(generate(numRows))

=======
Suggestion 8

def generate(numRows):
    #create list of lists
    result = [[1]]
    #loop through the rows
    for i in range(1, numRows):
        #create the row
        row = [1]
        #loop through the columns
        for j in range(1, i):
            #add the sum of the previous row's j and j-1
            row.append(result[i-1][j] + result[i-1][j-1])
        #add the last 1 to the row
        row.append(1)
        #add the row to the result
        result.append(row)
    return result

print(generate(5))
print(generate(1))
print(generate(0))
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
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
