Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                #print(i, j)
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        #print(dp)
        return max(dp)

=======
Suggestion 2

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] <= dp[j]:
                        dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 3

def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] is the length of LIS ending at nums[i]
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    # dp[i] = max(dp[i], dp[j] + 1)
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 4

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

=======
Suggestion 5

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 6

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
        return max(dp)

=======
Suggestion 7

def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

=======
Suggestion 8

def lengthOfLIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                # i番目の数字よりも前にある数字の方が小さい場合
                if nums[j] < nums[i]:
                    # その数字のdpに1を足したものと、現在のdpを比較する
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

=======
Suggestion 9

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        #単純にループを回していって，増加している部分を数える
        #例えば，[10,9,2,5,3,7,101,18]の場合
        #10,9,2,5,3,7,101,18
        #10,9,2,
