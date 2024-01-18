class Solution:
    def canCross(self, stones: list[int]) -> bool:
        return self.canCross_recur(0, 0, stones)

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))