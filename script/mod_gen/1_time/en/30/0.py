class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        if len(stones) == 3:
            return True
        if stones[2] != 3:
            return False
        max_jump = 2
        for i in range(3, len(stones)):
            if stones[i] - stones[i-1] > max_jump + 1:
                return False
            if stones[i] - stones[i-1] > max_jump:
                max_jump += 1
        return True

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))