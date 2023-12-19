def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        result = [[1], [1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result
print(generate(5))
print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(30))
