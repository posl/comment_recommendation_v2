class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1: return False
        dp = [set() for _ in range(len(stones))]
        dp[1].add(1)
        for i in range(2, len(stones)):
            for j in range(1, i):
                diff = stones[i] - stones[j]
                if diff in dp[j]:
                    dp[i].add(diff)
                    dp[i].add(diff + 1)
                    dp[i].add(diff - 1)
        return len(dp[-1]) > 0

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))