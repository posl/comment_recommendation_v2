Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        dp = [0] * len(envelopes)
        for envelope in envelopes:
            l, r = 0, ans
            while l < r:
                m = (l + r) // 2
                if dp[m] < envelope[1]:
                    l = m + 1
                else:
                    r = m
            dp[l] = envelope[1]
            if l == ans:
                ans += 1
        return ans

=======
Suggestion 3

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #dp[i] = i番目の封筒を使った時のロシア人形の最大数
        dp = [1] * len(envelopes)
        #幅でソートする
        envelopes.sort(key=lambda x: x[0])
        for i in range(len(envelopes)):
            for j in range(i):
                #i番目の封筒の幅がj番目の封筒の幅より大きく、i番目の封筒の高さがj番目の封筒の高さより大きい場合
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    #dp[i] = max(dp[i], dp[j] + 1)
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #print("envelopes:",envelopes)
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        #print("envelopes:",envelopes)
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        #print("dp:",dp)
        return max(dp)

=======
Suggestion 5

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

=======
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 二分探索で解く
        # まず、幅でソートし、幅が同じ場合は高さの降順でソートする
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        # この時点で、幅が同じ場合は高さの降順でソートされているため、
        # 高さに関しては最長増加部分列を求めれば良い
        # なお、幅が同じ場合は高さの降順でソートしているため、
        # 同じ幅の封筒を選ぶことはできない
        # 例：[[1, 2], [1, 3], [1, 4]]
        # この場合、高さが最大の[1, 4]を選ぶことはできても、
        # 次に高さが2番目に大きい[1, 3]を選ぶことはできない
        # なぜなら、幅が同じ場合は高さの降順でソートしているため、
        # 高さが2番目に大きい[1, 3]の幅は高さが最大の[1, 4]の幅よりも小さいため
        # [1, 3]を選ぶことができない
        nums = [x[1] for x in envelopes]
        # 最長増加部分列を求める
        # 二分探索を使うことでO(NlogN)で計算できる
        # なお、二分探索を使わない場合はO(N^2)で計算することになりTLEになる
        # 二分探索の解説は以下がわかりやすい
        # https://qiita

=======
Suggestion 7

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1. dp[i] = 0 とする
        dp = [1] * len(envelopes)
        # 2. ソートする
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # 3. dp[i] = max(dp[i], dp[j] + 1) if j < i and envelopes[j] < envelopes[i]
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # 4. max(dp)を返す
        return max(dp)

=======
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 要素数が0の場合は0を返す
        if len(envelopes) == 0:
            return 0
        # 要素数が1の場合は1を返す
        if len(envelopes) == 1:
            return 1
        # バブルソートで幅の小さい順にソートする
        for i in range(len(envelopes)):
            for j in range(len(envelopes) - i - 1):
                if envelopes[j][0] > envelopes[j+1][0]:
                    tmp = envelopes[j]
                    envelopes[j] = envelopes[j+1]
                    envelopes[j+1] = tmp
        # 封筒の数を数える
        count = 1
        # 2つ目の封筒の高さを保存する変数
        height = envelopes[0][1]
        # 2つ目の封筒の高さより大きい封筒があれば封筒の数をカウントアップする
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > height:
                height = envelopes[i][1]
                count += 1
        # 封筒の数を返す
        return count

=======
Suggestion 10

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # envelopes = [[w1,h1],[w2,h2],...,[wn,hn]]
        # w1 < w2 < ... < wn
        # h1 < h2 < ... < hn
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
        # w1 < h1
        # w2 < h2
        # ...
        # wn < hn
        # となるように並び替える
        # このとき、w1 < w2 < ... < wn なので、
