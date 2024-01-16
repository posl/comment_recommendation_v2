Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]

=======
Suggestion 2

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True
        return False

=======
Suggestion 3

def canPartition(self, nums: list[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        dp = [[False] * (target + 1) for i in range(len(nums) + 1)]
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums)][target]

=======
Suggestion 4

def canPartition(self, nums: list[int]) -> bool:
        # if sum is odd, return false
        if sum(nums) % 2 != 0:
            return False
        
        # create dp array
        dp = [[False for _ in range(sum(nums) // 2 + 1)] for _ in range(len(nums) + 1)]
        
        # initialize dp array
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        # iterate through dp array and update values
        for i in range(1, len(nums) + 1):
            for j in range(1, sum(nums) // 2 + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    if dp[i - 1][j - nums[i - 1]]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i - 1][j]
        
        # return last value of dp array
        return dp[len(nums)][sum(nums) // 2]

=======
Suggestion 5

def canPartition(self, nums: list[int]) -> bool:
        nums.sort()
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        dp = [False for i in range(half+1)]
        dp[0] = True
        for num in nums:
            for i in range(half, num-1, -1):
                dp[i] |= dp[i-num]
        return dp[-1]

=======
Suggestion 6

def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]

=======
Suggestion 7

def canPartition(self, nums: list[int]) -> bool:
        # Time Complexity: O(n * s)
        # Space Complexity: O(s)
        # s = sum(nums)
        # if s % 2 == 1:
        #     return False
        # s //= 2
        # dp = [False] * (s + 1)
        # dp[0] = True
        # for num in nums:
        #     for i in range(s, num - 1, -1):
        #         dp[i] |= dp[i - num]
        # return dp[s]
        # Time Complexity: O(n * s)
        # Space Complexity: O(s)
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[s]
        # Time Complexity: O(n * s)
        # Space Complexity: O(s)
        # s = sum(nums)
        # if s % 2 == 1:
        #     return False
        # s //= 2
        # dp = [False] * (s + 1)
        # dp[0] = True
        # for num in nums:
        #     for i in range(s, num - 1, -1):
        #         dp[i] |= dp[i - num]
        # return dp[s]
        # Time Complexity: O(n * s)
        # Space Complexity: O(s)
        # s = sum(nums)
        # if s % 2 == 1:
        #     return False
        # s //= 2
        # dp = [False] * (s + 1)
        # dp[0] = True
        # for num in nums:
        #     for i in range(s, num - 1, -1):
        #         dp[i] |= dp[i - num]
        # return dp[s]
        # Time Complexity: O(n * s)
        # Space Complexity: O(s)
        # s = sum(nums)
        # if s % 2 == 1:
        #     return False
        # s //= 2
        # dp = [False]

=======
Suggestion 8

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
        return dp[-1]

=======
Suggestion 9

def canPartition(self, nums: list[int]) -> bool:
        #sum of array must be even
        #if it is odd then it can't be divided into two equal subsets
        sumOfArray = sum(nums)
        if sumOfArray % 2 != 0:
            return False
        #if sum of array is even then it can be divided into two equal subsets
        #so we will find the subset whose sum is half of the sum of array
        #if such subset is found then it means that the array can be divided into two equal subsets
        #otherwise it can't be divided into two equal subsets
        sumOfSubset = sumOfArray // 2
        #we will use dynamic programming approach
        #we will create a 2d array dp of size (len(nums)+1) * (sumOfSubset+1)
        #dp[i][j] will represent whether the sum j can be formed using the first i elements of the array
        dp = [[False for j in range(sumOfSubset+1)] for i in range(len(nums)+1)]
        #if sum is 0 then it can be formed using any subset of the array
        for i in range(len(nums)+1):
            dp[i][0] = True
        #if sum is not 0 but array is empty then it can't be formed
        for j in range(1, sumOfSubset+1):
            dp[0][j] = False
        #now we will fill the dp array
        #if sum is less than or equal to the current element then we have two choices
        #we can either include the current element or we can exclude the current element
        #if we include the current element then we will check if the sum can be formed using the remaining elements
        #if we exclude the current element then we will check if the sum can be formed using the remaining elements
        for i in range(1, len(nums)+1):
            for j in range(1, sumOfSubset+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                elif nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
        #return the value of dp[len(nums)][sumOfSubset]
        return dp[len(nums)][sum
