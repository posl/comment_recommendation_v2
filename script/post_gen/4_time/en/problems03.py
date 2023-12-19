Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
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

rowIndex = 3
print(getRow(rowIndex))

rowIndex = 0
print(getRow(rowIndex))

rowIndex = 1
print(getRow(rowIndex))

rowIndex = 2
print(getRow(rowIndex))

rowIndex = 33
print(getRow(rowIndex))

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
        prev = [1,1]
        for i in range(2,rowIndex+1):
            curr = [1]
            for j in range(1,i):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            prev = curr
        return prev

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
Suggestion 3

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    prev_row = [1,1]
    for i in range(2,rowIndex+1):
        curr_row = [1]
        for j in range(1,i):
            curr_row.append(prev_row[j-1]+prev_row[j])
        curr_row.append(1)
        prev_row = curr_row
    return curr_row

=======
Suggestion 4

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for i in range(1,rowIndex+1):
        row.append(int(row[i-1]*(rowIndex+1-i)/i))
    return row

=======
Suggestion 5

def getRow(rowIndex):
    #create list of zeros
    result = [0] * (rowIndex + 1)
    #set first element to 1
    result[0] = 1
    #loop through rowIndex
    for i in range(rowIndex + 1):
        #loop through row backwards
        for j in range(i, 0, -1):
            #add current value to previous value
            result[j] = result[j] + result[j - 1]
    #return result
    return result

=======
Suggestion 6

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
        prev = [1,1]
        for i in range(2,rowIndex+1):
            curr = [1]
            for j in range(1,i):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            prev = curr
        return prev

=======
Suggestion 7

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
        ans = [1,1]
        for i in range(2,rowIndex+1):
            ans.append(0)
            for j in range(i,0,-1):
                ans[j] = ans[j] + ans[j-1]
        return ans

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
print(getRow(

=======
Suggestion 8

def getRow(rowIndex):
    result = []
    for i in range(rowIndex+1):
        temp = [1]*(i+1)
        for j in range(1,i):
            temp[j] = result[i-1][j-1] + result[i-1][j]
        result.append(temp)
    return result[rowIndex]
    
print(getRow(3))
print(getRow(0))
print(getRow(1))
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
print(getRow(67))
print(getRow(68))
print(getRow(69))
print(getRow(70))
print(getRow(71))
print(getRow(

=======
Suggestion 9

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # initialize the list with 1
    out = [1]
    # loop through the rowIndex
    for i in range(rowIndex):
        # initialize a temp list with 1
        temp = [1]
        # loop through the out list
        for j in range(len(out)-1):
            # append the sum of the current and next element
            temp.append(out[j] + out[j+1])
        # append the last 1
        temp.append(1)
        # update the out list
        out = temp
    # return the out list
    return out

=======
Suggestion 10

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    
    if rowIndex == 1:
        return [1,1]
    
    res = [1,1]
    for i in range(2, rowIndex+1):
        temp = [1]
        for j in range(1, len(res)):
            temp.append(res[j-1] + res[j])
        temp.append(1)
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
