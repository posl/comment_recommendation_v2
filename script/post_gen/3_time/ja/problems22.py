Synthesizing 10/10 solutions

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 2

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1. sort envelopes by width
        # 2. find longest increasing subsequence of heights
        envelopes.sort(key=lambda x: x[0])
        heights = [x[1] for x in envelopes]
        return self.lengthOfLIS(heights)

=======
Suggestion 3

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        size = 0

        for _, h in envelopes:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if dp[m] < h:
                    i = m + 1
                else:
                    j = m
            dp[i] = h
            size = max(i + 1, size)

        return size

=======
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        def binary_search(tails, num):
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] == num:
                    return mid
                elif tails[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        tails = []
        for _, h in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            if not tails or tails[-1] < h:
                tails.append(h)
            else:
                tails[binary_search(tails, h)] = h
        return len(tails)

=======
Suggestion 5

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 二分探索
        # envelopesを幅で昇順、高さで降順にソート
        # 幅が同じであれば高さの降順でソートされる
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp[i]はi番目の封筒を最後に使ったときのロシア人形の最大数
        dp = []
        for i, e in enumerate(envelopes):
            # e[1]は高さ
            # 二分探索でe[1]をdpに挿入する位置を探す
            # 挿入位置はe[1]より大きい最小の数の位置
            # e[1]がdpの最大値より大きい場合はdpの最後に追加する
            idx = bisect.bisect_left(dp, e[1])
            if idx == len(dp):
                dp.append(e[1])
            else:
                dp[idx] = e[1]
        return len(dp)

=======
Suggestion 7

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 基本的にはdpで解く
        # ただし、wの昇順、hの降順にソートする
        # その後、hに対してdpを行う
        # この場合、wは昇順にソートされているため、wに関しては考慮する必要がない
        # hに関しては、dp[i] = max(dp[i], dp[j] + 1 if h[i] > h[j])となる
        # ここで、i < jとなるようにする
        # また、dpは0で初期化しておく
        # この場合、dpの最大値が答えとなる
        # タイムスタンプはO(NlogN + N^2)となる
        # 空間計算量はO(N)となる
        # ここで、dpの計算を行う際に、二分探索を用いることで、タイムスタンプはO(NlogN)となる
        # 二分探索による実装は、下記の通り
        # ここで、dp[i] = hの長さがi+1のものの中で最小の値とする
        # この場合、二分探索により、dpの更新を行う際に、dp[i-1] < h[i] < dp[i]となるようにdpを更新する
        # そのため、dpの最大値が答えとなる
        # タイムスタンプはO(NlogN)となる
        # 空間計算量はO(N)となる
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        dp_size = 0
        for i in range(len(envelopes)):
            # 二分探索
            left = 0

=======
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #要素をソートする
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        #print(envelopes)
        #dpを初期化する
        dp = [0] * len(envelopes)
        #dpのインデックスを初期化する
        index = 0
        #dpのループを回す
        for i in range(len(envelopes)):
            #dpのインデックスを初期化する
            index = 0
            #dpのループを回す
            for j in range(i):
                #dpの条件分岐
                if envelopes[i][1] > envelopes[j][1]:
                    #dpのインデックスを更新する
                    index = max(index, dp[j])
            #dpのインデックスを更新する
            dp[i] = index + 1
        #dpの最大値を返す
        return max(dp)

=======
Suggestion 10

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #幅でソートする
        envelopes.sort(key=lambda x:x[0])
        #高さの昇順でソートする
        envelopes.sort(key=lambda x:x[1])

        #DP用の配列
        dp = [1] * len(envelopes)
        #DPを実行する
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #最大値を返す
        return max(dp)
