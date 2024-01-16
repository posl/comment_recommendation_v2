Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        dp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] > nums[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        # O(n^2) time complexity
        # O(n) space complexity
        # dp[i] = max(dp[j]) + 1, where 0 <= j < i and nums[j] < nums[i]
        # dp[i] = 1, where 0 <= j < i and nums[j] >= nums[i]
        # return max(dp)
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
        # O(nlogn) time complexity
        # O(n) space complexity
        # tails[i] = the minimum tail of the increasing subsequence of length i + 1
        # tails[i] = nums[j], where 0 <= j < i and nums[j] is the smallest number that can be the tail of the increasing subsequence of length i + 1
        # tails[i] = tails[i - 1], where nums[i] <= tails[i - 1]
        # tails[i] = nums[i], where nums[i] > tails[i - 1]
        # return the length of tails
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num: left = mid + 1
                else: right = mid
            tails[left] = num
            size = max(size, left + 1)
        return size

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)
