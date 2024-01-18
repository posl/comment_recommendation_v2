Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            ans = [[1],[1,1]]
            for i in range(2,rowIndex+1):
                tmp = [1]
                for j in range(1,i):
                    tmp.append(ans[i-1][j-1]+ans[i-1][j])
                tmp.append(1)
                ans.append(tmp)
            return ans[rowIndex]

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        ans = []
        for i in range(rowIndex + 1):
            ans.append([0] * (i + 1))
            ans[i][0] = 1
            ans[i][-1] = 1
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans[-1]

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1,1]
        for i in range(2, rowIndex+1):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ans[j-1] + ans[j])
            tmp.append(1)
            ans = tmp
        return ans

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1,1]
            for i in range(1,rowIndex):
                row = [1] + [row[i-1]+row[i] for i in range(1,len(row))] + [1]
            return row

=======
Suggestion 5

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #パスカルの三角形の性質を利用して解く
        #三角形の性質として、n行目の要素はn-1行目の要素を用いて求められる
        #n行目のi列目の要素はn-1行目のi-1列目の要素とi列目の要素の和となる
        #また、n行目のi列目の要素はn行目のi-1列目の要素とi列目の要素の和となる
        #上記の性質を利用すると、n行目の要素は、n-1行目の要素を用いて求められる
        #また、n行目の要素を求める際には、n-1行目の要素を更新してしまうと、
        #n-1行目の要素を用いてn行目の要素を求められなくなるため、
        #n行目の要素を求める際には、n-1行目の要素をコピーしておく必要がある
        #n行目の要素を求める際には、n-1行目の要素を用いて求められるため、
        #n行目の要素を求める際には、n-1行目の要素をコピーしておく必要がある
        #n行目の要素を求める際には、n-1行目の要素を用いて求められるため、
        #n行目の要素を求める際には、n-1行目の要素をコピーしておく必要がある
        #n行目の要素を求める際には、n-1行目の要素を用いて求められるため、
        #n行目の要素を求める際には、n-1行目の要素をコ

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(1, rowIndex+1):
            result = [1] + [result[j]+result[j+1] for j in range(len(result)-1)] + [1]
        return result

=======
Suggestion 7

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            ans = [1,1]
            for i in range(2,rowIndex+1):
                ans.append(1)
                for j in range(i-1,0,-1):
                    ans[j] = ans[j] + ans[j-1]
            return ans

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for i in range(rowIndex):
            result.append(result[i] * (rowIndex - i) // (i + 1))
        return result

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        #パスカルの三角形を作成する関数
        def pascal(n):
            #パスカルの三角形の初期値
            pascal_list = [[1]]
            for i in range(1,n+1):
                #n番目の行の初期値
                row_list = [1]
                #n番目の行の初期値を作成
                for j in range(1,i):
                    row_list.append(pascal_list[i-1][j-1]+pascal_list[i-1][j])
                #n番目の行の末尾に1を追加
                row_list.append(1)
                #n番目の行をpascal_listに追加
                pascal_list.append(row_list)
            return pascal_list
        return pascal(rowIndex)[rowIndex]

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
                cur = [1]
                for j in range(1,i):
                    cur.append(prev[j-1]+prev[j])
                cur.append(1)
                prev = cur
            return cur
