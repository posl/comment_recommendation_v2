class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.countOne(i))
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countBits(n))