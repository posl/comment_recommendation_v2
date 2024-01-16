class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(n+1):
            result.append(self.getOneCount(i))
        return result

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countBits(n))