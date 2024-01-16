Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            arr = [1,1]
            for i in range(2,rowIndex+1):
                newArr = [1]
                for j in range(1,i):
                    newArr.append(arr[j-1]+arr[j])
                newArr.append(1)
                arr = newArr
            return arr

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [1,1]
            for i in range(2,rowIndex+1):
                row = [1]
                for j in range(i-1):
                    row.append(result[j]+result[j+1])
                row.append(1)
                result = row
            return result

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        ans = [1]
        for i in range(rowIndex):
            ans = [x + y for x, y in zip([0] + ans, ans + [0])]
        return ans

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            l = [0]*(rowIndex+1)
            l[0] = 1
            l[1] = 1
            for i in range(2,rowIndex+1):
                for j in range(i,0,-1):
                    l[j] = l[j] + l[j-1]
            return l

=======
Suggestion 5

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            lst = [1,1]
            for i in range(2,rowIndex+1):
                new_lst = [1]
                for j in range(1,i):
                    new_lst.append(lst[j-1]+lst[j])
                new_lst.append(1)
                lst = new_lst
            return lst

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            prev_row = [1,1]
            for i in range(2,rowIndex+1):
                new_row = [1]
                for j in range(1,len(prev_row)):
                    new_row.append(prev_row[j-1]+prev_row[j])
                new_row.append(1)
                prev_row = new_row
            return prev_row

=======
Suggestion 7

def getRow(self, rowIndex: int) -> list[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            ans.append(int(ans[-1] * (rowIndex - i + 1) / i))
        return ans

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            lastRow = self.getRow(rowIndex-1)
            row = [1]
            for i in range(len(lastRow)-1):
                row.append(lastRow[i]+lastRow[i+1])
            row.append(1)
            return row

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            result = [[1],[1,1]]
            for i in range(2, rowIndex+1):
                temp = [1]
                for j in range(1, i):
                    temp.append(result[i-1][j-1] + result[i-1][j])
                temp.append(1)
                result.append(temp)
            return result[rowIndex]

=======
Suggestion 10

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        i = 2
        j = 2
        row = [1,1]
        while i <= rowIndex:
            row = [1] + [row[j] + row[j-1] for j in range(1,i)] + [1]
            i += 1
        return row
