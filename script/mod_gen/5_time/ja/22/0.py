class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        dp = [1] * len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = Solution()
    print(a.maxEnvelopes(envelopes))