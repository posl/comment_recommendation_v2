class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = n / 2
            else:
                if n == 3:
                    n = 2
                elif (n + 1) % 4 == 0:
                    n = n + 1
                else:
                    n = n - 1
            count = count + 1
        return count

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))