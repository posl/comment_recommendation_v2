Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max (dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        #O(n^2) time complexity
        #O(n) space complexity
        #dp[i] = max(dp[j]) + 1 for j in range(i) if nums[i] > nums[j]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        # O(n^2) solution
        # if len(nums) == 0:
        #     return 0
        # dp = [1]
        # for i in range(1, len(nums)):
        #     max_val = 0
        #     for j in range(0, i):
        #         if nums[j] < nums[i]:
        #             max_val = max(max_val, dp[j])
        #     dp.append(max_val + 1)
        # return max(dp)

        # O(n logn) solution
        # if len(nums) == 0:
        #     return 0
        # dp = []
        # for i in range(len(nums)):
        #     if len(dp) == 0 or nums[i] > dp[-1]:
        #         dp.append(nums[i])
        #     else:
        #         left, right = 0, len(dp)-1
        #         while left < right:
        #             mid = (left + right) // 2
        #             if dp[mid] < nums[i]:
        #                 left = mid + 1
        #             else:
        #                 right = mid
        #         dp[right] = nums[i]
        # return len(dp)

        # O(n logn) solution
        if len(nums) == 0:
            return 0
        dp = []
        for i in range(len(nums)):
            if len(dp) == 0 or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                left, right = 0, len(dp)-1
                while left < right:
                    mid = (left + right) // 2
                    if dp[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                dp[right] = nums[i]
        return len(dp)
