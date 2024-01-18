Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        dp = [1] * len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 2

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for i in range(len(envelopes)):
            left = 0
            right = len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid][1] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid
            if right == len(dp):
                dp.append(envelopes[i])
            else:
                dp[right] = envelopes[i]
        return len(dp)

=======
Suggestion 3

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for w, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

=======
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        size = 0
        for _, h in envelopes:
            i = bisect.bisect_left(dp, h, 0, size)
            dp[i] = h
            if i == size:
                size += 1
        return size

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
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        size = 0
        for _, h in envelopes:
            l = 0
            r = size
            while l < r:
                m = (l + r) // 2
                if dp[m] < h:
                    l = m + 1
                else:
                    r = m
            dp[l] = h
            if l == size:
                size += 1
        return size

=======
Suggestion 7

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        for w, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

=======
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        #ここから書きましょう
        return 0
