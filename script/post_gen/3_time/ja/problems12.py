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
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 3

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i, num in enumerate(nums):
            for j in range(i):
                if num % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [num]
        return max(dp, key=len)

=======
Suggestion 4

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j])+1:
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)

=======
Suggestion 5

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        dp[0].append(nums[0])
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = dp[j][:]
            dp[i].append(nums[i])
        dp.sort(key=len)
        return dp[-1]

=======
Suggestion 6

def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        ans = []
        for i in range(len(nums)):
            tmp = [nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%tmp[-1] == 0:
                    tmp.append(nums[j])
            if len(tmp) > len(ans):
                ans = tmp
        return ans
