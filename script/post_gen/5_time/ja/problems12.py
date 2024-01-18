Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:

=======
Suggestion 2

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
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key = len)

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i],dp[j]+1)
        max_num = max(dp)
        max_index = dp.index(max_num)
        ans = []
        for i in range(len(nums)-1,max_index-1,-1):
            if dp[i] == max_num:
                ans.append(nums[i])
                max_num -= 1
        return ans

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) <= len(dp[j]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 6

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 7

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0: dp[i] = max(dp[i], dp[j] + 1)
        maxLen = max(dp)
        maxVal = max(nums)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if dp[i] == maxLen and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxLen -= 1
        return res[::-1]

=======
Suggestion 8

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 9

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)
