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
