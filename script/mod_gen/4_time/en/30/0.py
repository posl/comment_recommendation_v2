class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if len(stones) < 2:
            return True
        elif len(stones) == 2:
            return stones[1] == 1
        else:
            return self.canCrossHelper(stones, 1, 1)

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))