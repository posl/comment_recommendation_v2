def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        triangle = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp = [1]
            for j in range(1,i-1):
                temp.append(triangle[i-2][j-1]+triangle[i-2][j])
            temp.append(1)
            triangle.append(temp)
        return triangle

if __name__ == '__main__':
    generate()