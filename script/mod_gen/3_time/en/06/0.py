class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.nthUglyNumber(n))