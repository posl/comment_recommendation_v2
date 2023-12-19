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
