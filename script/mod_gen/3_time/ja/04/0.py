class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = bin(i).count('1')
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countBits(n))