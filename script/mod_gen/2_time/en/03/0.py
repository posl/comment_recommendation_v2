class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1,rowIndex+1):
            row.append(int(row[i-1]*(rowIndex-i+1)/i))
        return row

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))