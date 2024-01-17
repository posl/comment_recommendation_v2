class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            arr = [1,1]
            for i in range(2,rowIndex+1):
                newArr = [1]
                for j in range(1,i):
                    newArr.append(arr[j-1]+arr[j])
                newArr.append(1)
                arr = newArr
            return arr

if __name__ == '__main__':
    rowIndex = int(input())
    a = Solution()
    print(a.getRow(rowIndex))