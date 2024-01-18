class Solution:
    def countDigitOne(self, n: int) -> int:
        # 1桁目の1の個数
        ans = 0
        # 10の桁数
        keta = 1
        # 1の桁数
        ones = 1
        while n >= keta:
            # 1の桁数 * 10の桁数
            ans += ones * (n // (keta * 10))
            # 1の桁数 * min(10の桁数, n % (10の桁数) + 1)
            ans += min(ones, n % (keta * 10) + 1)
            # 1の桁数を1つ増やす
            ones *= 10
            # 10の桁数を1つ増やす
            keta *= 10
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countDigitOne(n))