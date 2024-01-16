Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum % 2 != 0:
            return False
        sum = sum // 2
        dp = [[False for _ in range(sum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, sum + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][sum]

=======
Suggestion 2

def canPartition(self, nums: list[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2 != 0:
            return False
        target = sumNums // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, target + 1):
            dp[0][i] = nums[0] == i

        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]]

        return dp[len(nums) - 1][target]

=======
Suggestion 3

def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 != 0:
            return False
        sum = sum // 2
        dp = [False] * (sum + 1)
        dp[0] = True
        for num in nums:
            for i in range(sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[sum]

=======
Suggestion 4

def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        target = sum_ // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

=======
Suggestion 5

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

=======
Suggestion 6

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]

=======
Suggestion 7

def canPartition(self, nums: list[int]) -> bool:
        nums.sort()
        sumNums = sum(nums)
        if sumNums % 2 == 1:
            return False
        target = sumNums // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
        return dp[len(nums)][target]

=======
Suggestion 8

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # 1. get the sum of the list
        # 2. if the sum is not even, return false
        # 3. if the sum is even, divide by 2 and check if the list contains the number
        # 4. if the sum is even, divide by 2 and check if the list contains the number
        # 5. if the sum is even, divide by 2 and check if the list contains the number
        # 6. if the sum is even, divide by 2 and check if the list contains the number
        # 7. if the sum is even, divide by 2 and check if the list contains the number
        # 8. if the sum is even, divide by 2 and check if the list contains the number
        # 9. if the sum is even, divide by 2 and check if the list contains the number
        # 10. if the sum is even, divide by 2 and check if the list contains the number
        # 11. if the sum is even, divide by 2 and check if the list contains the number
        # 12. if the sum is even, divide by 2 and check if the list contains the number
        # 13. if the sum is even, divide by 2 and check if the list contains the number
        # 14. if the sum is even, divide by 2 and check if the list contains the number
        # 15. if the sum is even, divide by 2 and check if the list contains the number
        # 16. if the sum is even, divide by 2 and check if the list contains the number
        # 17. if the sum is even, divide by 2 and check if the list contains the number
        # 18. if the sum is even, divide by 2 and check if the list contains the number
        # 19. if the sum is even, divide by 2 and check if the list contains the number
        # 20. if the sum is even, divide by 2 and check if the list contains the number
        # 21. if the sum is even, divide by 2 and check if the list contains the number
        # 22. if the sum is even, divide by 2 and

=======
Suggestion 9

def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]
