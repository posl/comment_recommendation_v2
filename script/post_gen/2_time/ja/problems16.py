Synthesizing 10/10 solutions

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i] := targetがiのときの組み合わせの数
        #dp[i] = sum(dp[i - num] for num in nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            dp[i] += sum(dp[i - num] for num in nums if i - num >= 0)
        return dp[target]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] := target = i となる組み合わせの数
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 8

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[-1]

=======
Suggestion 9

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i]:targetがiのときの組み合わせの数
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for num in nums:
                if i-num>=0:
                    dp[i]+=dp[i-num]
        return dp[target]

=======
Suggestion 10

def combinationSum4(self, nums: list[int], target: int) -> int:
        #dp[i] := targetがiの時の組み合わせの数
        #dp[i] = dp[i-nums[0]] + dp[i-nums[1]] + ... + dp[i-nums[n]]
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]
