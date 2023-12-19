def pascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(result[i-1][j-1] + result[i-1][j])
            temp.append(1)
            result.append(temp)
        return result

if __name__ == '__main__':
    pascalTriangle()