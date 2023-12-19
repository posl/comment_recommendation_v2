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
