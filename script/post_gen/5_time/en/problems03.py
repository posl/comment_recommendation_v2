Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        lst = [1]
        for i in range(1, rowIndex+1):
            lst.append(int(lst[i-1]*(rowIndex-i+1)/i))
        return lst

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            row = [1,2,1]
            for i in range(2,rowIndex):
                newRow = [1]
                for j in range(1,len(row)):
                    newRow.append(row[j-1]+row[j])
                newRow.append(1)
                row = newRow
            return row

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        triangle = [[1],[1,1]]
        if rowIndex == 0:
            return triangle[0]
        elif rowIndex == 1:
            return triangle[1]
        else:
            for i in range(1,rowIndex):
                triangle.append([1])
                for j in range(1,i+1):
                    triangle[i+1].append(triangle[i][j-1] + triangle[i][j])
                triangle[i+1].append(1)
            return triangle[rowIndex]

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(rowIndex):
            row.append(row[i] * (rowIndex - i) // (i + 1))
        return row

=======
Suggestion 5

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            res=[1,1]
            for i in range(2,rowIndex+1):
                temp=[1]
                for j in range(len(res)-1):
                    temp.append(res[j]+res[j+1])
                temp.append(1)
                res=temp
            return res

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(rowIndex):
            result.append(result[i] * (rowIndex - i) // (i + 1))
        return result

=======
Suggestion 7

def getRow(self, rowIndex: int) -> list[int]:
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
            return [1,16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1820,560,120

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        #Solution 1
        #row = [1]
        #for i in range(rowIndex):
        #    row = [x + y for x, y in zip([0] + row, row + [0])]
        #return row
        
        #Solution 2
        row = [1]
        for i in range(rowIndex):
            row.append(int(row[i] * (rowIndex - i) / (i + 1)))
        return row
        
        #Solution 3
        row = [1]
        for i in range(rowIndex):
            row.append(row[i] * (rowIndex - i) // (i + 1))
        return row

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        row = [1,1]
        for i in range(2,rowIndex+1):
            row = [1] + [row[j]+row[j+1] for j in range(i-1)] + [1]
        return row

=======
Suggestion 10

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev = [1,1]
            for i in range(2,rowIndex+1):
                temp = [1]
                for j in range(1,i):
                    temp.append(prev[j-1]+prev[j])
                temp.append(1)
                prev = temp
            return prev
