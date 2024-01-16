Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
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
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        dp = [0]*len(envelopes)
        size = 0
        for w, h in envelopes:
            l, r = 0, size
            while l != r:
                mid = (l + r)//2
                if dp[mid] < h:
                    l = mid + 1
                else:
                    r = mid
            dp[l] = h
            size = max(size, l + 1)
        return size

=======
Suggestion 4

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)

        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

=======
Suggestion 5

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
Suggestion 6

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        dp = []
        for i in range(len(envelopes)):
            left, right = 0, len(dp)
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
        h = []
        for i in envelopes:
            if not h or i[1] > h[-1]:
                h.append(i[1])
            else:
                l, r = 0, len(h) - 1
                while l < r:
                    mid = (l + r) // 2
                    if h[mid] < i[1]:
                        l = mid + 1
                    else:
                        r = mid
                h[l] = i[1]
        return len(h)

=======
Suggestion 9

def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
