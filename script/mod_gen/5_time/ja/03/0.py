class Solution:
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

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))