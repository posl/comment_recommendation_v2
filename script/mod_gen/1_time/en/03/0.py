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

if __name__ == '__main__':
    getRow()