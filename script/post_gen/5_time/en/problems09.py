Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        subsum = total // 2
        dp = [[False for _ in range(subsum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, subsum + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
        return dp[-1][-1]

=======
Suggestion 2

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
Suggestion 3

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[target]

=======
Suggestion 4

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]

=======
Suggestion 5

def canPartition(self, nums: list[int]) -> bool:
        # sum(nums) must be even
        if sum(nums)%2 != 0:
            return False
        # initialize a dp array with False
        dp = [False]*(sum(nums)//2+1)
        # the first element in dp array must be True
        dp[0] = True
        # iterate through the nums array
        for num in nums:
            # iterate through the dp array
            for j in range(len(dp)-1, -1, -1):
                # if the current element in dp array is True
                # and if the current element in nums array
                # is less than or equal to the current element in dp array
                if dp[j] and num+j <= len(dp)-1:
                    # set the element in dp array to True
                    dp[num+j] = True
        # return the last element in dp array
        return dp[-1]

=======
Suggestion 6

def canPartition(self, nums: list[int]) -> bool:
        sum = 0
        for i in nums:
            sum += i
        if sum % 2 != 0:
            return False
        sum = sum // 2
        dp = [[False for x in range(sum + 1)] for y in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, sum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][sum]

=======
Suggestion 7

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][target]

=======
Suggestion 8

def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
