class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []
        for i in range(numRows):
            pascal.append([1]*(i+1))
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))