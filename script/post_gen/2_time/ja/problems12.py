Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        maxLen = 1
        maxIdx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > maxLen:
                maxLen = dp[i]
                maxIdx = i
        ans = []
        while maxIdx != -1:
            ans.append(nums[maxIdx])
            maxIdx = prev[maxIdx]
        return ans

=======
Suggestion 2

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j]+1,dp[i])
        max_value = max(dp)
        max_index = dp.index(max_value)
        result = []
        for i in range(max_index,-1,-1):
            if dp[i] == max_value and nums[max_index] % nums[i] == 0:
                result.append(nums[i])
                max_value -= 1
        return result

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        max_len = 1
        max_idx = 0
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if max_len < dp[i]:
                max_len = dp[i]
                max_idx = i
        ans = []
        while max_idx != -1:
            ans.append(nums[max_idx])
            max_idx = prev[max_idx]
        return ans[::-1]

=======
Suggestion 6

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
