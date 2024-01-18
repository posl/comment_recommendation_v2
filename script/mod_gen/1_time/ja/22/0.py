class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1.ソートする
        # 2.二分探索で最長増加部分列を求める
        # 3.最長増加部分列の長さを求める
        # 4.最長増加部分列の長さを返す
        # 5.終わり
        # 1.ソートする
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # 2.二分探索で最長増加部分列を求める
        # 3.最長増加部分列の長さを求める
        # 4.最長増加部分列の長さを返す
        # 5.終わり
        return self.binarySearch(envelopes)

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = Solution()
    print(a.maxEnvelopes(envelopes))