class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        lst = [1]
        for i in range(1, rowIndex+1):
            lst.append(int(lst[i-1]*(rowIndex-i+1)/i))
        return lst

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))