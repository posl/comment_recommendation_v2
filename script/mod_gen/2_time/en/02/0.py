class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result

if __name__ == '__main__':
    numRows = int(input())
    a = Solution()
    print(a.generate(numRows))