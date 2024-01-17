class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        stones = set(stones)
        self.memo = {}
        def dfs(i, k):
            if i == stones[-1]:
                return True
            if (i, k) in self.memo:
                return self.memo[(i, k)]
            if k <= 0:
                return False
            for j in (k - 1, k, k + 1):
                if i + j in stones:
                    if dfs(i + j, j):
                        self.memo[(i + j, j)] = True
                        return True
            self.memo[(i, k)] = False
            return False
        return dfs(1, 1)

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))