class Solution:
    def countBits(self, n: int) -> list[int]:
        # リストの作成
        ans = [0] * (n + 1)
        # 配列の長さ分ループ
        for i in range(n + 1):
            # リストに値を入れる
            ans[i] = bin(i).count('1')
        return ans

if __name__ == '__main__':
    n = int(input())
    a = Solution()
    print(a.countBits(n))