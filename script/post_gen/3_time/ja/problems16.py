Synthesizing 10/10 solutions

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for n in nums:
                if t - n >= 0:
                    dp[t] += dp[t - n]
        return dp[target]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] = target が i になる組み合わせの数
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        return dp[target]

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i-j]
        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in range(1, target + 1):
            for i in range(len(nums)):
                if num >= nums[i]:
                    dp[num] += dp[num - nums[i]]
        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        # DP
        # dp[i] = targetがiになる組み合わせの数
        # dp[i] = sum(dp[i - num] for num in nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i] := target = i になるような組み合わせの数
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 8

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # numsの要素の和がtargetとなる組み合わせの数を返す
        # 組み合わせの順序を考慮する
        # numsの要素はすべて異なる
        # numsの要素はすべて正の整数
        # targetは正の整数
        # 1 <= nums.length <= 200
        # 1 <= nums[i] <= 1000
        # 1 <= target <= 1000
        # 答えは32ビット整数に収まる
        # メモ化再帰で解く
        # dp[i] := iを作る組み合わせの数
        # dp[i] = dp[i - j] + dp[j] (j in nums)
        # 初期値：dp[0] = 1
        # 答え：dp[target]
        # 0 <= i <= target
        # 0 <= j <= i
        # dp[i] = dp[i - j] + dp[j] (j in nums)
        # dp[0] = 1
        # dp[1] = dp[0] + dp[1 - 1] = 1 + 1 = 2
        # dp[2] = dp[1] + dp[2 - 1] = 2 + 1 = 3
        # dp[3] = dp[2] + dp[3 - 1] = 3 + 1 = 4
        # dp[4] = dp[3] + dp[4 - 1] = 4 + 1 = 5
        # dp[5] = dp[4] + dp[5 - 1] = 5 + 1 = 6
        # dp[6] = dp[5] + dp[6 - 1] = 6 + 1 = 7
        # dp[7] = dp[6] + dp[7 - 1] = 7 + 1 = 8
        # dp[8] = dp[7] + dp[8 - 1] = 8 + 1 = 9

=======
Suggestion 9

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        
        return dp[target]

=======
Suggestion 10

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp = [0]*(target+1)
        #dp[0] = 1
        #for i in range(1, target+1):
        #    for num in nums:
        #        if i-num >= 0:
        #            dp[i] += dp[i-num]
        #return dp[target]
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]
