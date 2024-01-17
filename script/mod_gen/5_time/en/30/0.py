class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for step in range(k-1, k+2):
                    if step > 0 and stone + step in dp:
                        dp[stone + step].add(step)
        return len(dp[stones[-1]]) > 0

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))