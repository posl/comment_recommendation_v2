def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    if rowIndex == 2:
        return [1,2,1]
    if rowIndex == 3:
        return [1,3,3,1]
    if rowIndex == 4:
        return [1,4,6,4,1]
    if rowIndex == 5:
        return [1,5,10,10,5,1]
    if rowIndex == 6:
        return [1,6,15,20,15,6,1]
    if rowIndex == 7:
        return [1,7,21,35,35,21,7,1]
    if rowIndex == 8:
        return [1,8,28,56,70,56,28,8,1]
    if rowIndex == 9:
        return [1,9,36,84,126,126,84,36,9,1]
    if rowIndex == 10:
        return [1,10,45,120,210,252,210,120,45,10,1]
    if rowIndex == 11:
        return [1,11,55,165,330,462,462,330,165,55,11,1]
    if rowIndex == 12:
        return [1,12,66,220,495,792,924,792,495,220,66,12,1]
    if rowIndex == 13:
        return [1,13,78,286,715,1287,1716,1716,1287,715,286,78,13,1]
    if rowIndex == 14:
        return [1,14,91,364,1001,2002,3003,3432,3003,2002,1001,364,91,14,1]
    if rowIndex == 15:
        return [1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1]
    if rowIndex == 16:
        return [1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,

if __name__ == '__main__':
    getRow()