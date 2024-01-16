Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+1, len(nums)-1):
                if nums[j+1] - nums[j] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result = 0
        dp = [Counter() for item in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [Counter() for item in nums]
        ans = 0
        for i in range(n):
            for j in range(i):
                delta = nums[i] - nums[j]
                dp[i][delta] += 1
                if delta in dp[j]:
                    dp[i][delta] += dp[j][delta]
                    ans += dp[j][delta]
        return ans

=======
Suggestion 4

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)
        ans = 0
        dp = [Counter() for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    ans += dp[j][diff]
        return ans

=======
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        dp = [defaultdict(int) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    ans += dp[j][diff]
        return ans

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Brute Force
        # Time: O(n^3)
        # Space: O(1)
        # n = len(nums)
        # count = 0
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         diff = nums[j] - nums[i]
        #         for k in range(j+1, n):
        #             if nums[k] - nums[j] == diff:
        #                 count += 1
        # return count

        # Dynamic Programming
        # Time: O(n^2)
        # Space: O(n^2)
        n = len(nums)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    count += dp[j][diff]
        return count

        # Dynamic Programming
        # Time: O(n^2)
        # Space: O(n^2)
        # n = len(nums)
        # count = 0
        # dp = [defaultdict(int) for _ in range(n)]
        # for i in range(1, n):
        #     for j in range(i):
        #         diff = nums[i] - nums[j]
        #         dp[i][diff] += 1
        #         if diff in dp[j]:
        #             dp[i][diff] += dp[j][diff]
        #             count += dp[j][diff]
        # return count

        # Dynamic Programming
        # Time: O(n^2)
        # Space: O(n^2)
        # n = len(nums)
        # count = 0
        # dp = [defaultdict(int) for _ in range(n)]
        # for i in range(1, n):
        #     for j in range(i):
        #         diff = nums[i] - nums[j]
        #         dp[i][diff] += 1
        #         if diff in dp[j]:
        #             dp[i][diff] += dp[j][diff]
        #             count += dp[j][diff]
        # return count

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [Counter() for item in nums]
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[j][d]
                ans += cnt
                dp[i][d] += cnt + 1
        return ans

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        dp = [Counter() for item in nums]
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]] + 1
                ans += dp[j][nums[i] - nums[j]]
        return ans

=======
Suggestion 9

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        #Brute Force
        #O(N^3) time and O(1) space
        #Time Limit Exceeded
        #subsequence = 0
        #for i in range(len(nums)):
        #    for j in range(i+1,len(nums)):
        #        for k in range(j+1,len(nums)):
        #            if nums[j] - nums[i] == nums[k] - nums[j]:
        #                subsequence += 1
        #return subsequence

        #Dynamic Programming
        #O(N^2) time and O(N) space
        #dp = [defaultdict(int) for _ in range(len(nums))]
        #subsequence = 0
        #for i in range(len(nums)):
        #    for j in range(i):
        #        diff = nums[i] - nums[j]
        #        dp[i][diff] += 1
        #        if diff in dp[j]:
        #            dp[i][diff] += dp[j][diff]
        #            subsequence += dp[j][diff]
        #return subsequence

        #Dynamic Programming
        #O(N^2) time and O(N) space
        #dp = [defaultdict(int) for _ in range(len(nums))]
        #subsequence = 0
        #for i in range(len(nums)):
        #    for j in range(i):
        #        diff = nums[i] - nums[j]
        #        dp[i][diff] += 1
        #        if diff in dp[j]:
        #            dp[i][diff] += dp[j][diff]
        #            subsequence += dp[j][diff]
        #return subsequence

        #Dynamic Programming
        #O(N^2) time and O(N) space
        #dp = [defaultdict(int) for _ in range(len(nums))]
        #subsequence = 0
        #for i in range(len(nums)):
        #    for j in range(i):
        #        diff = nums[i] - nums[j]
        #        dp[i][diff] += 1
        #        if diff in dp[j]:
        #            dp[i][diff] += dp[j][diff]
        #            subsequence += dp[j][diff]
        #return subsequence

        #Dynamic Programming
        #O(N^2) time and O(N) space

=======
Suggestion 10

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += 1
                if d in dp[j]:
                    dp[i][d] += dp[j][d]
                    res += dp[j][d]
        return res
