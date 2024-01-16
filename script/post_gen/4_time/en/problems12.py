Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 2

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
        index = dp.index(max(dp))
        subset = [nums[index]]
        for i in range(index, -1, -1):
            if subset[-1]%nums[i] == 0 and dp[i] == dp[index]-1:
                subset.append(nums[i])
                index = i
        return subset[::-1]

=======
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        maxSubsetSize = 1
        maxSubsetIndex = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > maxSubsetSize:
                maxSubsetSize = dp[i]
                maxSubsetIndex = i
        subset = []
        while maxSubsetIndex != -1:
            subset.append(nums[maxSubsetIndex])
            maxSubsetIndex = prev[maxSubsetIndex]
        return subset[::-1]

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[i])<len(dp[j])+1:
                    dp[i] = dp[j]+[nums[i]]
        return max(dp, key=len)

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        max_index = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] +1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[max_index] < dp[i]:
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        return result[::-1]

=======
Suggestion 6

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp = [1] * len(nums)
        parent = [-1] * len(nums)
        max_index = 0
        max_count = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if max_count < dp[i]:
                max_count = dp[i]
                max_index = i
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = parent[max_index]
        return res[::-1]

=======
Suggestion 7

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
