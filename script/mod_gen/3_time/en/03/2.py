def getRow(rowIndex):
    # 1st solution
    #time complexity O(n^2)
    #space complexity O(n^2)
    # if rowIndex == 0:
    #     return [1]
    # elif rowIndex == 1:
    #     return [1,1]
    # else:
    #     triangle = [[1],[1,1]]
    #     for i in range(2,rowIndex+1):
    #         row = [1]
    #         for j in range(1,i):
    #             row.append(triangle[i-1][j-1]+triangle[i-1][j])
    #         row.append(1)
    #         triangle.append(row)
    #     return triangle[rowIndex]
    # 2nd solution
    #time complexity O(n^2)
    #space complexity O(n)
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1,1]
    else:
        row = [1,1]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                row[j] = row[j-1]+row[j]
            row.append(1)
        return row

if __name__ == '__main__':
    getRow()