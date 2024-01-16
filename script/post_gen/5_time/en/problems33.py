Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                diff = nums[j] - nums[i]
                for k in range(j + 1, len(nums)):
                    if nums[k] - nums[j] == diff:
                        count += 1
                    elif nums[k] - nums[j] > diff:
                        break
        return count

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        dp = [defaultdict(int) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += 1
                if nums[i] - nums[j] in dp[j]:
                    dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]]
                    ans += dp[j][nums[i] - nums[j]]
        return ans

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # dp[i][d] -> number of subsequences ending at i with difference d
        # dp[i][d] = sum(dp[j][d]) for all j < i
        # ans = sum(dp[i][d]) for all i
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += 1
                if d in dp[j]:
                    dp[i][d] += dp[j][d]
                    ans += dp[j][d]
        return ans

=======
Suggestion 4

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
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
        count = 0
        for i in range(1, len(nums) - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(nums):
                if nums[left] + nums[right] == 2 * nums[i]:
                    left -= 1
                    right += 1
                    count += 1
                elif nums[left] + nums[right] > 2 * nums[i]:
                    left -= 1
                else:
                    right += 1
        return count

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        def numSlices(n):
            return (n * (n - 1)) // 2

        def numSlicesWithLength(n):
            return (n * (n - 1)) // 2 - (n - 1)

        if len(nums) < 3:
            return 0

        dp = [{} for _ in range(len(nums))]
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 1
                if dp[j][diff] >= 2:
                    ans += dp[j][diff] - 1
        return ans

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                ans += dp[j][d]
                dp[i][d] += dp[j][d] + 1
        return ans

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return ans

=======
Suggestion 9

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # 1. Brute Force
        # 2. DP
        # 3. DP with 2D matrix
        # 4. DP with 1D matrix
        # 5. DP with 1D matrix and constant space
        # 6. Math
        # 7. Two Pointers
        # 8. Set
        # 9. Recursion
        # 10. Recursion with memorization
        # 11. Bitmask
        # 12. Bitmask with memorization
        # 13. Sliding Window
        # 14. Sliding Window with set
        # 15. Sliding Window with set and memorization
        # 16. Sliding Window with 2 pointers
        # 17. Sliding Window with 2 pointers and set
        # 18. Sliding Window with 2 pointers and set and memorization
        # 19. Sliding Window with 2 pointers and set and memorization and binary search
        # 20. Sliding Window with 2 pointers and set and memorization and binary search and bitmask
        # 21. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion
        # 22. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math
        # 23. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math and DP
        # 24. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math and DP and 1D DP
        # 25. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math and DP and 1D DP and 2D DP
        # 26. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math and DP and 1D DP and 2D DP and 2D DP with bitmask
        # 27. Sliding Window with 2 pointers and set and memorization and binary search and bitmask and recursion and math and DP and 1D DP and 2D DP and 2D DP with bitmask and 2D DP with bitmask and recursion
        # 28

=======
Suggestion 10

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # dp[i][j] = number of arithmetic subsequences ending at i with difference j
        # dp[i][j] = sum(dp[k][j] + 1) for k < i and nums[k] + j == nums[i]
        # ans = sum(dp[i][j] for i in range(len(nums)) for j in range(nums[i] - nums[0] + 1))
        dp = [Counter() for _ in nums]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                ans += dp[j][diff]
        return ans
