class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 4
        else:
            if n%3==0:
                return 3**(n//3)
            elif n%3==1:
                return 3**(n//3-1)*4
            else:
                return 3**(n//3)*2

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.integerBreak(n))