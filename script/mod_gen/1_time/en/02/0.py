def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    if numRows >= 3:
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
            pascal.append(row)
        return pascal

if __name__ == '__main__':
    generate()