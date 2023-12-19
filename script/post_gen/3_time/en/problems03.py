Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    result = [1,1]
    for i in range(2, rowIndex+1):
        temp = [1]
        for j in range(1, i):
            temp.append(result[j-1] + result[j])
        temp.append(1)
        result = temp
    return result

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(8))
print(getRow(9))
print(getRow(10))
print(getRow(11))
print(getRow(12))
print(getRow(13))
print(getRow(14))
print(getRow(15))
print(getRow(16))
print(getRow(17))
print(getRow(18))
print(getRow(19))
print(getRow(20))
print(getRow(21))
print(getRow(22))
print(getRow(23))
print(getRow(24))
print(getRow(25))
print(getRow(26))
print(getRow(27))
print(getRow(28))
print(getRow(29))
print(getRow(30))
print(getRow(31))
print(getRow(32))
print(getRow(33))

=======
Suggestion 2

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev_row = [1,1]
        for i in range(2,rowIndex+1):
            temp_row = [1]
            for j in range(1,len(prev_row)):
                temp_row.append(prev_row[j-1]+prev_row[j])
            temp_row.append(1)
            prev_row = temp_row
        return temp_row

=======
Suggestion 3

def getRow(rowIndex):
    # 1st solution
    #time complexity O(n^2)
    #space complexity O(n^2)
    # if rowIndex == 0:
    #     return [1]
    # elif rowIndex == 1:
    #     return [1,1]
    # else:
    #     triangle = [[1],[1,1]]
    #     for i in range(2,rowIndex+1):
    #         row = [1]
    #         for j in range(1,i):
    #             row.append(triangle[i-1][j-1]+triangle[i-1][j])
    #         row.append(1)
    #         triangle.append(row)
    #     return triangle[rowIndex]

    # 2nd solution
    #time complexity O(n^2)
    #space complexity O(n)
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        row = [1,1]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                row[j] = row[j-1]+row[j]
            row.append(1)
        return row

=======
Suggestion 4

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    else:
        previousRow = [1,1]
        for i in range(2,rowIndex+1):
            currentRow = [1]
            for j in range(1,i):
                currentRow.append(previousRow[j-1]+previousRow[j])
            currentRow.append(1)
            previousRow = currentRow
        return currentRow

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(4))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(8))
print(getRow(9))
print(getRow(10))
print(getRow(11))
print(getRow(12))
print(getRow(13))
print(getRow(14))
print(getRow(15))
print(getRow(16))
print(getRow(17))
print(getRow(18))
print(getRow(19))
print(getRow(20))
print(getRow(21))
print(getRow(22))
print(getRow(23))
print(getRow(24))
print(getRow(25))
print(getRow(26))
print(getRow(27))
print(getRow(28))
print(getRow(29))
print(getRow(30))
print(getRow(31))
print(getRow(32))
print(getRow(33))

=======
Suggestion 5

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    res = [1,1]
    for i in range(2,rowIndex+1):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(res[j-1]+res[j])
        res = temp
    return res

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(4))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(8))
print(getRow(9))

=======
Suggestion 6

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    else:
        result = [1,1]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(result[j-1]+result[j])
            temp.append(1)
            result = temp
        return result

print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
print(getRow(5))

=======
Suggestion 7

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    #create a list of lists
    pascal = [[1]*(i+1) for i in range(rowIndex+1)]
    for i in range(rowIndex+1):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal[rowIndex]
    
#Time complexity: O(n^2)
#Space complexity: O(n^2)

=======
Suggestion 8

def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
    return row

=======
Suggestion 9

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for i in range(1, rowIndex+1):
        row.append(int(row[i-1]*(rowIndex+1-i)/i))
    return row

=======
Suggestion 10

def getRow(rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        if rowIndex == 2: return [1,2,1]
        row = [1,2,1]
        for i in range(2,rowIndex):
            newRow = [1]
            for j in range(1,len(row)):
                newRow.append(row[j-1]+row[j])
            newRow.append(1)
            row = newRow
        return row

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(4))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(8))
print(getRow(9))
print(getRow(10))
print(getRow(11))
print(getRow(12))
print(getRow(13))
print(getRow(14))
print(getRow(15))
print(getRow(16))
print(getRow(17))
print(getRow(18))
print(getRow(19))
print(getRow(20))
print(getRow(21))
print(getRow(22))
print(getRow(23))
print(getRow(24))
print(getRow(25))
print(getRow(26))
print(getRow(27))
print(getRow(28))
print(getRow(29))
print(getRow(30))
print(getRow(31))
print(getRow(32))
print(getRow(33))
print(getRow(34))
print(getRow(35))
print(getRow(36))
print(getRow(37))
print(getRow(38))
print(getRow(39))
print(getRow(40))
print(getRow(41))
print(getRow(42))
print(getRow(43))
print(getRow(44))
print(getRow(45))
print(getRow(46))
print(getRow(47))
print(getRow(48))
print(getRow(49))
print(getRow(50))
print(getRow(51))
print(getRow(52))
print(getRow(53))
print(getRow(54))
print(getRow(55))
print(getRow(56))
print(getRow(57))
print(getRow(58))
print(getRow(59))
print(getRow(60))
print(getRow(61))
print(getRow(62
