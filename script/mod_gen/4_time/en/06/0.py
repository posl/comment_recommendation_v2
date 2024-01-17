class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while n > 1:
            n2 = ugly[i2] * 2
            n3 = ugly[i3] * 3
            n5 = ugly[i5] * 5
            min_ugly = min(n2, n3, n5)
            if min_ugly == n2:
                i2 += 1
            if min_ugly == n3:
                i3 += 1
            if min_ugly == n5:
                i5 += 1
            ugly.append(min_ugly)
            n -= 1
        return ugly[-1]

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.nthUglyNumber(n))