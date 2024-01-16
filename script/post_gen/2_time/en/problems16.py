Synthesizing 10/10 solutions

=======
Suggestion 1

def combinationSum4(self, nums: list[int], target: int) -> int:
        # DP
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]

=======
Suggestion 2

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, target + 1):
            for j in nums:
                if j > i:
                    break
                dp[i] += dp[i - j]
        return dp[-1]

=======
Suggestion 3

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]

=======
Suggestion 4

def combinationSum4(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i-j >= 0:
                    dp[i] += dp[i-j]
        return dp[-1]

=======
Suggestion 5

def combinationSum4(self, nums: list[int], target: int) -> int:
        # Dynamic programming
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for num in nums:
                if i - num < 0:
                    break
                dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 6

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

=======
Suggestion 7

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[target]

=======
Suggestion 8

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]

=======
Suggestion 9

def combinationSum4(self, nums: list[int], target: int) -> int:
        # 1. DP
        # dp[i] = dp[i - nums[0]] + dp[i - nums[1]] + dp[i - nums[2]] + ... + dp[i - nums[n]]
        # dp[i] = sum(dp[i - nums[j]]), j = 0, 1, 2, ..., n
        # dp[0] = 1
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        return dp[target]

        # 2. Recursion + Memoization
        # memo = {}
        # def dfs(remain):
        #     if remain in memo:
        #         return memo[remain]
        #     if not remain:
        #         return 1
        #     res = 0
        #     for num in nums:
        #         if remain >= num:
        #             res += dfs(remain - num)
        #     memo[remain] = res
        #     return res
        # return dfs(target)

        # 3. Recursion + Memoization
        # memo = {}
        # def dfs(remain):
        #     if remain in memo:
        #         return memo[remain]
        #     if not remain:
        #         return 1
        #     res = 0
        #     for num in nums:
        #         if remain >= num:
        #             res += dfs(remain - num)
        #     memo[remain] = res
        #     return res
        # return dfs(target)

        # 4. Recursion
        # if not target:
        #     return 1
        # res = 0
        # for num in nums:
        #     if target >= num:
        #         res += self.combinationSum4(nums, target - num)
        # return res

        # 5. Recursion + Memoization
        # memo = {}
        # def dfs(remain):
        #     if remain in memo:
        #         return memo[remain]
        #     if not remain:
        #         return 1
        #     res = 0
        #     for num in nums:
        #         if

=======
Suggestion 10

def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]
