Synthesizing 10/10 solutions

=======
Suggestion 1

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
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

print(generate(5))

=======
Suggestion 2

def generate(numRows):
    result = [[1]]
    for i in range(1, numRows):
        result.append([1])
        for j in range(1, i):
            result[i].append(result[i-1][j-1] + result[i-1][j])
        result[i].append(1)
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
Suggestion 3

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1],[1,1]]
    res = [[1],[1,1]]
    for i in range(2,numRows):
        temp = [1]
        for j in range(1,i):
            temp.append(res[i-1][j-1]+res[i-1][j])
        temp.append(1)
        res.append(temp)
    return res

=======
Suggestion 4

def generate(numRows):
    pascal = []
    for i in range(numRows):
        pascal.append([1]*(i+1))
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

=======
Suggestion 5

def pascalTriangle(numRows):
    #create empty list
    result = []
    #loop through the number of rows
    for i in range(numRows):
        #create an empty list
        row = []
        #loop through the range of i + 1
        for j in range(i + 1):
            #if j is equal to 0 or j is equal to i
            if j == 0 or j == i:
                #append 1 to row
                row.append(1)
            #else
            else:
                #append the sum of the previous row and the current row to row
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        #append row to result
        result.append(row)
    #return result
    return result

=======
Suggestion 6

def generate(numRows):
    result = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result

print(generate(5))
print(generate(1))

=======
Suggestion 7

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

numRows = 5
print(generate(numRows))
numRows = 1
print(generate(numRows))
numRows = 2
print(generate(numRows))
numRows = 3
print(generate(numRows))

=======
Suggestion 8

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
        triangle = [[1],[1,1]]
        for i in range(2,numRows):
            triangle.append([1])
            for j in range(1,i):
                triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle[i].append(1)
        return triangle

print(generate(5))

=======
Suggestion 9

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
        res = [[1],[1,1]]
        for i in range(2,numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j-1]+res[i-1][j])
            res.append(row)
        return res

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
Suggestion 10

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
            result.append([1])
            for j in range(1,i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
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
print(generate(30))
print(generate(31))
print(generate(32))
print(generate(33))
print(generate(34))
print(generate(35))
print(generate(36))
print(generate(37))
print(generate(38))
print(generate(39))
print(generate(40))
