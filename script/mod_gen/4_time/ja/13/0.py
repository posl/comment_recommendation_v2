class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                cnt += 1
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
                cnt += 1
            else:
                n += 1
                cnt += 1
        return cnt

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))