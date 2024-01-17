class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 10:
            return 1
        res = 0
        n = str(n)
        for i in range(len(n)):
            if i == 0:
                if int(n[i]) > 1:
                    res += 10 ** (len(n) - 1)
                elif int(n[i]) == 1:
                    res += int(n[i + 1:]) + 1
            elif i == len(n) - 1:
                if int(n[i]) >= 1:
                    res += 1
            else:
                if int(n[i]) > 1:
                    res += (int(n[:i]) + 1) * 10 ** (len(n) - i - 1)
                elif int(n[i]) == 1:
                    res += int(n[:i]) * 10 ** (len(n) - i - 1) + int(n[i + 1:]) + 1
        return res

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))