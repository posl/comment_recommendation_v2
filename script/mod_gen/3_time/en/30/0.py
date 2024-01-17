class Solution:
    def canCross(self, stones: list[int]) -> bool:
        return self.canCrossRec(stones, 0, 0)

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))