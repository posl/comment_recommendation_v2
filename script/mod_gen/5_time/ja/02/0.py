class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            ans = [[1],[1,1]]
            for i in range(2,numRows):
                tmp = [1]
                for j in range(i-1):
                    tmp.append(ans[i-1][j]+ans[i-1][j+1])
                tmp.append(1)
                ans.append(tmp)
            return ans

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))