Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            idx = bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)

=======
Suggestion 2

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1]*len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1]<envelopes[i][1] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)

=======
Suggestion 3

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
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if len(envelopes) == 0: return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] > envelopes[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

=======
Suggestion 5

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        dp = []
        for i in range(len(envelopes)):
            l, r = 0, len(dp) - 1
            while l <= r:
                mid = (l + r) // 2
                if dp[mid][1] < envelopes[i][1]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(dp):
                dp.append(envelopes[i])
            else:
                dp[l] = envelopes[i]
        return len(dp)

=======
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if len(envelopes) == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 7

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
Suggestion 8

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0 for _ in range(len(envelopes))]
        size = 0
        for _, h in envelopes:
            l, r = 0, size
            while l < r:
                mid = l + (r - l) // 2
                if dp[mid] < h:
                    l = mid + 1
                else:
                    r = mid
            dp[l] = h
            if l == size:
                size += 1
        return size

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for i in range(len(envelopes)):
            idx = bisect.bisect_left(dp, envelopes[i][1])
            if idx == len(dp):
                dp.append(envelopes[i][1])
            else:
                dp[idx] = envelopes[i][1]
        return len(dp)
