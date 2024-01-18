import bisect
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp = [float("inf")]*len(envelopes)
        for i in range(len(envelopes)):
            dp[bisect.bisect_left(dp,envelopes[i][1])] = envelopes[i][1]
        return bisect.bisect_left(dp, float("inf"))

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = Solution()
    print(a.maxEnvelopes(envelopes))