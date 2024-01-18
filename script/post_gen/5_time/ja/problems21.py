Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    ans += 1
                else:
                    break
        return ans

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        #解答
        ans = 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
        return ans

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                count += dp[i]
        return count

=======
Suggestion 4

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    result += 1
                else:
                    break
        return result

=======
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        for i in range(1, len(nums)-1):
            diff = nums[i] - nums[i-1]
            for j in range(i+1, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    ans += 1
                else:
                    break
        return ans

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # dp[i] = 0 ~ i までの等差数列の数
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # dp[i - 1] までの等差数列の数 + [nums[i - 2], nums[i - 1], nums[i]] の数
                dp[i] = dp[i - 1] + 1
        return sum(dp)

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] != nums[i+1] - nums[i]:
                    break
                ans += 1
        return ans

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans += 1
        return ans

=======
Suggestion 9

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        dp = [0] * n
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
        return ans

=======
Suggestion 10

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            d = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] == d:
                    ans += 1
                else:
                    break
        return ans
