def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    elif numRows == 3:
        return [[1], [1, 1], [1, 2, 1]]
    elif numRows == 4:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    elif numRows == 5:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    elif numRows == 6:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    elif numRows == 7:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1]]
    elif numRows == 8:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
    elif numRows == 9:
        return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1,

if __name__ == '__main__':
    generate()