class Solution:
    def canCross(self, stones: list[int]) -> bool:
        #初期値
        dp = [[False] * len(stones) for _ in range(len(stones))]
        dp[0][0] = True
        #初期値以外
        for i in range(1, len(stones)):
            for j in range(i):
                k = stones[i] - stones[j]
                #kがstonesの長さより大きい場合はFalse
                if k > i:
                    continue
                #kの値が存在する場合はTrue
                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                #最後の石にたどり着けたらTrue
                if i == len(stones) - 1 and dp[i][k]:
                    return True
        return False

if __name__ == '__main__':
    stones = list(map(int, input().split()))
    a = Solution()
    print(a.canCross(stones))