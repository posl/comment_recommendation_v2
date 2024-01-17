class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for i in range(2,numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1]+result[i-1][j])
            result.append(temp)
        return result

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))