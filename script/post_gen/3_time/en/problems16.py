Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        #print(nums, target)
        if target == 0:
            return 1
        if target < 0:
            return 0
        result = 0
        for i in nums:
            result += self.combinationSum4(nums, target - i)
        return result

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(len(dp)):
            for num in nums:
                if num > i:
                    continue
                elif num == i:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - num]
        return dp[-1]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]
        return dp[target]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if num > i: break
                dp[i] += dp[i - num]
        return dp[target]
