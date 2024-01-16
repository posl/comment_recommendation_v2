Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            temp = [1]
            for j in range(1,i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res[rowIndex]

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev = [1,1]
            for i in range(2,rowIndex+1):
                curr = [1]
                for j in range(1,i):
                    curr.append(prev[j-1]+prev[j])
                curr.append(1)
                prev = curr
            return curr

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            output = [[1],[1,1]]
            for i in range(2,rowIndex+1):
                temp = [1]
                for j in range(1,i):
                    temp.append(output[i-1][j-1]+output[i-1][j])
                temp.append(1)
                output.append(temp)
            return output[rowIndex]

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        lst = [1]
        for i in range(1,rowIndex+1):
            lst = [1] + [lst[j]+lst[j+1] for j in range(i-1)] + [1]
        return lst

=======
Suggestion 5

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev = self.getRow(rowIndex-1)
            return [1] + [prev[i] + prev[i+1] for i in range(rowIndex-1)] + [1]

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1,1]
            for i in range(2,rowIndex+1):
                newRow = [1]
                for j in range(1,i):
                    newRow.append(row[j-1]+row[j])
                newRow.append(1)
                row = newRow
            return row

=======
Suggestion 7

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in range(2,rowIndex+1):
            tmp = [1]
            for j in range(1,i):
                tmp.append(res[j-1]+res[j])
            tmp.append(1)
            res = tmp
        return res

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        #defining the first row
        row = [1]
        #looping through the row index
        for i in range(rowIndex):
            #creating the next row
            row = [x+y for x,y in zip([0]+row, row+[0])]
        #returning the row
        return row

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1,1]
            for i in range(2, rowIndex+1):
                new_row = [1]
                for j in range(len(row)-1):
                    new_row.append(row[j]+row[j+1])
                new_row.append(1)
                row = new_row
            return row

=======
Suggestion 10

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        if rowIndex == 3:
            return [1,3,3,1]
        output = [1,3,3,1]
        for i in range(4,rowIndex+1):
            temp = [1]
            for j in range(1,i-1):
                temp.append(output[j-1]+output[j])
            temp.append(1)
            output = temp
        return output
