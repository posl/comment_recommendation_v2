class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            current = [1,1]
            for i in range(2, rowIndex+1):
                previous = current.copy()
                current = [1]
                for j in range(1, i):
                    current.append(previous[j-1] + previous[j])
                current.append(1)
            return current

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))