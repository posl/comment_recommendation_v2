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
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        mx = 0
        mx_idx = 0
        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if mx < dp[i]:
                mx = dp[i]
                mx_idx = i
        res = []
        while mx_idx != -1:
            res.append(nums[mx_idx])
            mx_idx = prev[mx_idx]
        return res[::-1]

=======
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1 for i in range(len(nums))]
        parent = [-1 for i in range(len(nums))]
        max_len = 1
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if max_len < dp[i]:
                max_len = dp[i]
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = parent[max_index]
        return res

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
        max_index = dp.index(max(dp))
        res = []
        cur = nums[max_index]
        for i in range(max_index,-1,-1):
            if cur % nums[i] == 0 and dp[max_index] == dp[i]:
                res.append(nums[i])
                cur = nums[i]
        return res[::-1]

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1]*len(nums)
        maxIndex = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
            if dp[i] > dp[maxIndex]:
                maxIndex = i
        prev = nums[maxIndex]
        ans = []
        for i in range(maxIndex,-1,-1):
            if prev%nums[i] == 0 and dp[maxIndex] == dp[i]:
                ans.append(nums[i])
                prev = nums[i]
                maxIndex -= 1
        return ans[::-1]

=======
Suggestion 6

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 7

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
