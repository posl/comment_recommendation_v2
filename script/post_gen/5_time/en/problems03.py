Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
        res = [1,1]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(res[j-1]+res[j])
            temp.append(1)
            res = temp
        return res

=======
Suggestion 2

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    else:
        return [1] + [sum(x) for x in zip(getRow(rowIndex-1), getRow(rowIndex-1)[1:])] + [1]
    
#Test Case
rowIndex = 4
print(getRow(rowIndex))

=======
Suggestion 3

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
        row = [1,1]
        for i in range(2,rowIndex+1):
            newRow = [1]
            for j in range(1,i):
                newRow.append(row[j-1]+row[j])
            newRow.append(1)
            row = newRow
        return row

=======
Suggestion 4

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev = [1,1]
        for i in range(2,rowIndex+1):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            prev = curr
        return curr

=======
Suggestion 5

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        prev = [1,1]
        for i in range(1,rowIndex):
            new = [1]
            for j in range(len(prev)-1):
                new.append(prev[j]+prev[j+1])
            new.append(1)
            prev = new
        return prev

=======
Suggestion 6

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex == 2:
        return [1,2,1]
    lst = [1,2,1]
    for i in range(2,rowIndex):
        lst.append(1)
        for j in range(i,0,-1):
            lst[j] = lst[j] + lst[j-1]
    return lst

print(getRow(3))

=======
Suggestion 7

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [[1],[1,1]]
    if rowIndex == 0:
        return res[0]
    if rowIndex == 1:
        return res[1]
    for i in range(1,rowIndex):
        temp = [1]
        for j in range(1,i+1):
            temp.append(res[i][j-1]+res[i][j])
        temp.append(1)
        res.append(temp)
    return res[rowIndex]

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
Suggestion 8

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex == 2:
        return [1,2,1]
    if rowIndex == 3:
        return [1,3,3,1]
    if rowIndex == 4:
        return [1,4,6,4,1]
    if rowIndex == 5:
        return [1,5,10,10,5,1]
    if rowIndex == 6:
        return [1,6,15,20,15,6,1]
    if rowIndex == 7:
        return [1,7,21,35,35,21,7,1]
    if rowIndex == 8:
        return [1,8,28,56,70,56,28,8,1]
    if rowIndex == 9:
        return [1,9,36,84,126,126,84,36,9,1]
    if rowIndex == 10:
        return [1,10,45,120,210,252,210,120,45,10,1]
    if rowIndex == 11:
        return [1,11,55,165,330,462,462,330,165,55,11,1]
    if rowIndex == 12:
        return [1,12,66,220,495,792,924,792,495,220,66,12,1]
    if rowIndex == 13:
        return [1,13,78,286,715,1287,1716,1716,1287,715,286,78,13,1]
    if rowIndex == 14:
        return [1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1]
    if rowIndex == 15:
        return [1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1]
    if rowIndex == 16:
        return [1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,

=======
Suggestion 9

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    prev = [1,1]
    for i in range(1,rowIndex):
        current = [1]
        for j in range(0,len(prev)-1):
            current.append(prev[j]+prev[j+1])
        current.append(1)
        prev = current
    return current
