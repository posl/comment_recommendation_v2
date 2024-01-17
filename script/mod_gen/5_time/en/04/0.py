class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(0, n+1):
            result.append(self.countOnes(i))
        return result

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countBits(n))