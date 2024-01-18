Synthesizing 10/10 solutions

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 2

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
Suggestion 3

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1. ソート
        # 2. 動的計画法
        # 3. 二分探索
        # 4. 二分探索 + 動的計画法
        # 5. ビット探索

        # 1. ソート
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)
        # dp = []
        # for _, h in envelopes:
        #     l = 0
        #     r = len(dp)
        #     while l < r:
        #         m = (l + r) // 2
        #         if dp[m] < h:
        #             l = m + 1
        #         else:
        #             r = m
        #     if r == len(dp):
        #         dp.append(h)
        #     else:
        #         dp[r] = h
        # return len(dp)

        # 2. 動的計画法
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp = [1] * len(envelopes)
        # for i in range(len(envelopes)):
        #     for j in range(i):
        #         if envelopes[i][1] > envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # 3. 二分探索
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            l = 0
            r = len(dp)
            while l < r:
                m = (l + r) // 2
                if dp[m] < h:
                    l = m + 1
                else:
                    r = m
            if r == len(dp):
                dp.append(h)
            else:
                dp[r] = h
        return len(dp)

        # 4. 二分探索 + 動的計画法
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp = [1] * len(envelopes)
        # for i in

=======
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 5

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if len(envelopes) == 1:
            return 1
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        size = 0
        for _, h in envelopes:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = h
            size = max(size, left + 1)
        return size

=======
Suggestion 7

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        dp = [1]*len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        for i in range(len(envelopes)):
            if not dp or envelopes[i][1] > dp[-1]:
                dp.append(envelopes[i][1])
            else:
                left, right = 0, len(dp) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[mid] < envelopes[i][1]:
                        left = mid + 1
                    else:
                        right = mid
                dp[left] = envelopes[i][1]
        return len(dp)

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #ここから書きましょう
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp=[envelopes[0][1]]
        for i in range(1,len(envelopes)):
            if envelopes[i][1]>dp[-1]:
                dp.append(envelopes[i][1])
            else:
                l=0
                r=len(dp)-1
                while l<r:
                    m=(l+r)//2
                    if dp[m]<envelopes[i][1]:
                        l=m+1
                    else:
                        r=m
                dp[l]=envelopes[i][1]
        return len(dp)

=======
Suggestion 10

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # envelopesをw_iで昇順ソートする
        envelopes.sort(key=lambda x: x[0])
        # dp[i] := 長さi+1の増加部分列の最後の要素の最小値
        dp = [float('inf')] * len(envelopes)
        for w, h in envelopes:
            # hがdpの最後の要素より大きい場合、dpの最後にhを追加する
            # それ以外の場合、dpの中でhより大きい最小の要素をhに置き換える
            # これにより、dpには常に最長の増加部分列が格納される
            i = bisect.bisect_left(dp, h)
            dp[i] = h
        # dpの長さが増加部分列の最大長になる
        return bisect.bisect_left(dp, float('inf'))
