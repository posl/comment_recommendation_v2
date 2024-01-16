Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in self.d:
            return self.d[target]
        ans = 0
        for i in range(len(nums)):
            ans += self.combinationSum4(nums, target - nums[i])
        self.d[target] = ans
        return ans

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]

        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for subtarget in range(1, target + 1):
            for num in nums:
                if subtarget - num >= 0:
                    dp[subtarget] += dp[subtarget - num]

        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(target+1):
            for num in nums:
                if i+num <= target:
                    dp[i+num] += dp[i]
        return dp[-1]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[-1]
