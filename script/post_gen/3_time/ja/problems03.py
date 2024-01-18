Synthesizing 10/10 solutions

=======
Suggestion 1

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [1,1]
            for i in range(rowIndex-1):
                result = self.calc(result)
            return result

=======
Suggestion 2

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            ans = [1,1]
            for i in range(rowIndex-1):
                ans.append(1)
                for j in range(len(ans)-2, 0, -1):
                    ans[j] = ans[j] + ans[j-1]
            return ans

=======
Suggestion 3

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        row = [1,2,1]
        for i in range(3,rowIndex+1):
            row = self.nextRow(row)
        return row

=======
Suggestion 4

def getRow(self, rowIndex: int) -> list[int]:
        #初期値
        answer = [[1]]
        #ループ処理
        for i in range(1, rowIndex + 1):
            #初期値
            tmp = [1]
            #ループ処理
            for j in range(1, i):
                #計算
                tmp.append(answer[i - 1][j - 1] + answer[i - 1][j])
            #計算
            tmp.append(1)
            #代入
            answer.append(tmp)
        #返却
        return answer[rowIndex]

=======
Suggestion 5

def getRow(self, rowIndex: int) -> list[int]:
        #パスカルの三角形の性質を利用する
        #出力するリストの要素数はrowIndex+1
        #リストの先頭と末尾は1
        #リストの要素の数が2以上の場合、2つのリストの要素を足した値をリストに追加する
        #リストの要素の数がrowIndex+1になるまで繰り返す
        #O(rowIndex)
        #S(rowIndex)
        #Runtime: 32 ms, faster than 77.05% of Python3 online submissions for Pascal's Triangle II.
        #Memory Usage: 14.2 MB, less than 75.65% of Python3 online submissions for Pascal's Triangle II.
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        #リストの先頭と末尾は1
        answer = [1,1]
        #リストの要素の数がrowIndex+1になるまで繰り返す
        while len(answer) < rowIndex + 1:
            #リストの要素の数が2以上の場合、2つのリストの要素を足した値をリストに追加する
            for i in range(len(answer)-1):
                answer[i] = answer[i] + answer[i+1]
            answer.insert(0,1)
        return answer

=======
Suggestion 6

def getRow(self, rowIndex: int) -> list[int]:
        answer = [1]
        for i in range(rowIndex):
            answer.insert(0,0)
            for j in range(i+1):
                answer[j] = answer[j] + answer[j+1]
        return answer

=======
Suggestion 7

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            ans = [1,1]
            for i in range(rowIndex-1):
                ans.append(1)
                for j in range(len(ans)-2,0,-1):
                    ans[j] = ans[j-1] + ans[j]
            return ans

=======
Suggestion 8

def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            ans = [1,1]
            for i in range(2,rowIndex+1):
                ans.insert(1,i)
                for j in range(2,i+1):
                    ans[j] = ans[j] + ans[j+1]
            return ans

=======
Suggestion 9

def getRow(self, rowIndex: int) -> list[int]:
        result = []
        for i in range(rowIndex+1):
            result.append(1)
            for j in range(i-1, 0, -1):
                result[j] = result[j-1] + result[j]
        return result

=======
Suggestion 10

def getRow(self, rowIndex: int) -> list[int]:
        res = [[1] * (i+1) for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[-1]
