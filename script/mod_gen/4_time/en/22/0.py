class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        return self.lengthOfLIS([i[1] for i in envelopes])

if __name__ == '__main__':
    envelopes = list(map(int, input().split()))
    envelopes = [envelopes[i:i+2] for i in range(0, len(envelopes), 2)]
    a = Solution()
    print(a.maxEnvelopes(envelopes))