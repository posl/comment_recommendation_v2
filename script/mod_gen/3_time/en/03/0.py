class Solution:
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

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))