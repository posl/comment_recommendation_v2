Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex >= 2:
        triangle = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            row = [1]
            for j in range(1,i):
                row.append(triangle[i-1][j-1]+triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle[rowIndex]
    return []

=======
Suggestion 2

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        result = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            row = [1]
            for j in range(1,i):
                row.append(result[i-1][j-1]+result[i-1][j])
            row.append(1)
            result.append(row)
        return result[rowIndex]
        
#test case
rowIndex = 3
print(getRow(rowIndex))

=======
Suggestion 3

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        prev_row = [1, 1]
        for i in range(2, rowIndex+1):
            curr_row = [1]
            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            curr_row.append(1)
            prev_row = curr_row
        return curr_row

print(getRow(3))
print(getRow(0))
print(getRow(1))
print(getRow(2))

=======
Suggestion 4

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        result = [1,1]
        for i in range(2, rowIndex+1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(result[j-1] + result[j])
            tmp.append(1)
            result = tmp
        return result

=======
Suggestion 5

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # Approach: Dynamic Programming
    # Time Complexity: O(rowIndex^2)
    # Space Complexity: O(rowIndex)
    # rowIndex = 0: [1]
    # rowIndex = 1: [1, 1]
    # rowIndex = 2: [1, 2, 1]
    # rowIndex = 3: [1, 3, 3, 1]
    # rowIndex = 4: [1, 4, 6, 4, 1]
    # rowIndex = 5: [1, 5, 10, 10, 5, 1]
    # rowIndex = 6: [1, 6, 15, 20, 15, 6, 1]
    # rowIndex = 7: [1, 7, 21, 35, 35, 21, 7, 1]
    # rowIndex = 8: [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # rowIndex = 9: [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    # rowIndex = 10: [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    # rowIndex = 11: [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
    # rowIndex = 12: [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
    # rowIndex = 13: [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]
    # rowIndex = 14: [1, 14, 91, 364, 1001, 2002, 3003, 3432,

=======
Suggestion 6

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for k in range(rowIndex):
        row.append(row[k] * (rowIndex-k) / (k+1))
    return row

print(getRow(3))
print(getRow(0))
print(getRow(1))

=======
Suggestion 7

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex > 1:
        prev = [1,1]
        for i in range(2,rowIndex+1):
            current = [1]
            for j in range(len(prev)-1):
                current.append(prev[j]+prev[j+1])
            current.append(1)
            prev = current
        return current

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
print(getRow(62))
print(getRow(63))
print(getRow(64))
print(getRow(65))
print(getRow(66

=======
Suggestion 8

def getRow(rowIndex):
    row = [1]
    for i in range(rowIndex):
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
    return row

=======
Suggestion 9

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        triangle = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            triangle.append([1]*(i+1))
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[rowIndex]

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
Suggestion 10

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    
    prev = [1,1]
    for i in range(2, rowIndex+1):
        curr = [1]
        for j in range(1, i):
            curr.append(prev[j-1] + prev[j])
        curr.append(1)
        prev = curr
        
    return curr

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
print(getRow(62))
print(getRow(63))
print(getRow(64))
print(getRow(65))
print(getRow(66))
print(getRow(
