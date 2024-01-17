class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n/2
                count += 1
            elif n == 3 or n % 4 == 1:
                n = n - 1
                count += 1
            else:
                n = n + 1
                count += 1
        return count

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerReplacement(n))