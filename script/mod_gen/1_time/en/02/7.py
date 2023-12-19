def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    else:
        result = [[1], [1,1]]
        for i in range(2, numRows):
            result.append([1])
            for j in range(1, i):
                result[i].append(result[i-1][j-1] + result[i-1][j])
            result[i].append(1)
        return result
print(generate(5))
