class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1, 1])
            else:
                row = [1]
                for j in range(1, i):
                    row.append(result[i - 1][j - 1] + result[i - 1][j])
                row.append(1)
                result.append(row)
        return result

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))