Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            maxLen = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, dp[j])
            dp.append(maxLen+1)
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        # O(n^2)
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # O(nlogn)
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
            else:
                left = 0
                right = len(dp) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                dp[left] = nums[i]
        return len(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = 1 + dp[j]
            max_len = max(max_len, dp[i])
        return max_len

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j]+1:
                    lis[i] = lis[j]+1
        return max(lis)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        return max(dp)
