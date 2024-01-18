Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(row[i - 1] * (rowIndex - i + 1) // i)
        return row

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        list = []
        for i in range(rowIndex+1):
            list.append(self.combination(rowIndex, i))
        return list

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        # パスカルの三角形を作成
        triangle = []
        for i in range(rowIndex + 1):
            triangle.append([0] * (i + 1))
            triangle[i][0] = 1
            triangle[i][i] = 1
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle[rowIndex]

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [1,1]
            for i in range(2,rowIndex+1):
                tmp = [1]
                for j in range(1,i):
                    tmp.append(result[j-1]+result[j])
                tmp.append(1)
                result = tmp
            return result

=======
Suggestion 5

def getRow(self, rowIndex: int) -> list[int]:
        ans = [[1]]
        for i in range(1,rowIndex+1):
            ans.append([1])
            for j in range(1,i):
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
            ans[i].append(1)
        return ans[rowIndex]

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        #ここから書きましょう
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            ans=[1,1]
            for i in range(2,rowIndex+1):
                tmp=ans[0]
                for j in range(1,len(ans)):
                    tmp2=ans[j]
                    ans[j]=tmp+ans[j]
                    tmp=tmp2
                ans.append(1)
            return ans

=======
Suggestion 7

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #パスカルの三角形の性質を利用して、
        #1行目は[1]、2行目は[1,1]、3行目は[1,2,1]というように、
        #n行目のリストは、n-1行目のリストの隣り合う要素の和になる
        #例えば、4行目は[1,3,3,1]で、[1,2,1]と[1,1]の要素を足している
        #ここで、[1,2,1]というリストを作るには、
        #1行目の[1]の前後に0を追加して[0,1,0]にし、
        #隣り合う要素を足して[1,1]にする
        #同様に、[1,1]の前後に0を追加して[0,1,1,0]にし、
        #隣り合う要素を足して[1,2,1]にする
        #同様に、[1,2,1]の前後に0を追加して[0,1,2,1,0]にし、
        #隣り合う要素を足して[1,3,3,1]にする
        #という手順で、n行目のリストを作ることができる
        #この手順をn回繰り返すと、n行目のリストが作れる
        #この手順を繰り返すには、n回のfor文が必要になる
        #パスカルの三角形の性質を利用して、
        #n回のfor文を1回のfor文に変えることができる
        #1回のfor文で、n行目のリストが作れる
        #1回のfor文で、n行目のリストを作る

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        #初期化
        ans = [0 for i in range(rowIndex+1)]
        ans[0] = 1
        for i in range(rowIndex+1):
            for j in range(i,0,-1):
                ans[j] += ans[j-1]
        return ans

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(1,rowIndex+1):
            result.append(int(result[i-1]*(rowIndex-i+1)/i))
        return result

=======
Suggestion 10

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1,1]
        for i in range(2,rowIndex+1):
            ans.append(1)
            for j in range(i-1,0,-1):
                ans[j] = ans[j-1] + ans[j]
        return ans
