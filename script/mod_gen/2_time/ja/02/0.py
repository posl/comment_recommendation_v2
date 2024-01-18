class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            pascal.append([1] + [pascal[i-1][j] + pascal[i-1][j+1] for j in range(i-1)] + [1])
        return pascal

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))