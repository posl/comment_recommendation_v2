Synthesizing 10/10 solutions

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp = [float("inf")]*len(envelopes)
        for i in range(len(envelopes)):
            dp[bisect.bisect_left(dp,envelopes[i][1])] = envelopes[i][1]
        return bisect.bisect_left(dp, float("inf"))

=======
Suggestion 2

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        return 0

=======
Suggestion 3

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
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 5

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # 1. dp[i] : i番目の封筒を使ったときの、ロシア人形の最大の長さ
        # 2. dp[i] = max(dp[i], dp[j] + 1) if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]
        # 3. dp[0] = 1
        # 4. O(N^2)
        # 5. 2つの値を比較するため、ソートする
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(h)
            else:
                dp[right] = h
        return len(dp)

=======
Suggestion 7

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
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # sort by width
        envelopes.sort(key=lambda x: x[0])
        dp = [1 for _ in range(len(envelopes))]
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 10

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
