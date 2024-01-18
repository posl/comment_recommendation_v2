class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = []
        for i in range(rowIndex+1):
            ans.append(self.comb(rowIndex,i))
        return ans

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))