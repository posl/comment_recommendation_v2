Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 2

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len, max_ind = 1, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_ind = i
        ans = []
        while max_ind != -1:
            ans.append(nums[max_ind])
            max_ind = prev[max_ind]
        return ans[::-1]

=======
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len = 0
        max_idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if max_len < dp[i]:
                max_len = dp[i]
                max_idx = i
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        return res

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] +1:
                    dp[i] = dp[j] +1
        max_index = dp.index(max(dp))
        res = [nums[max_index]]
        for i in range(max_index, -1, -1):
            if res[-1] % nums[i] == 0 and dp[max_index] - dp[i] == 1:
                res.append(nums[i])
                max_index = i
        return res[::-1]

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[i]) <= len(dp[j]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
