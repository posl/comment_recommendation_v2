def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
            result.append(temp)
        return result

if __name__ == '__main__':
    generate()