class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            pascal = [[1],[1,1]]
            for i in range(2,numRows):
                pascal.append([1])
                for j in range(1,i):
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
                pascal[i].append(1)
            return pascal

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))