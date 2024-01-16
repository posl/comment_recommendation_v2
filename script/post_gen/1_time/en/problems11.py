Synthesizing 10/10 solutions

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        # O(n^2)
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # O(nlogn)
        dp = []
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                left, right = 0, len(dp) - 1
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[mid] >= num:
                        right = mid
                    else:
                        left = mid + 1
                dp[left] = num
        return len(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                #print(nums[i], nums[j])
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    #print(dp)
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        maxans = 1
        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res

=======
Suggestion 9

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                #check if nums[i] is greater than nums[j]
                #check if the current dp[i] is less than dp[j] + 1
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    #update dp[i]
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 10

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
