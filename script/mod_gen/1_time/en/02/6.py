def generate(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1,1]]
    elif numRows == 3:
        return [[1], [1,1], [1,2,1]]
    elif numRows == 4:
        return [[1], [1,1], [1,2,1], [1,3,3,1]]
    elif numRows == 5:
        return [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
print(generate(5))
