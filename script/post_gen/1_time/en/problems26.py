Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        #print(nums, k)
        if len(nums) == 1: return nums[0]
        if k == 1: return sum(nums)
        if k == len(nums): return max(nums)
        if k == 2:
            return max(sum(nums[:i]) for i in range(1, len(nums)))
        else:
            for i in range(1, len(nums)):
                if self.splitArray(nums[i:], k - 1) < self.splitArray(nums[i:], k):
                    return self.splitArray(nums[i:], k - 1)
            return self.splitArray(nums, k - 1)

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        dp = [[0 for _ in range(len(nums))] for _ in range(k)]
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[0][i] = dp[0][i - 1] + nums[i]
        for i in range(1, k):
            for j in range(i, len(nums)):
                dp[i][j] = min(max(dp[i - 1][k - 1], dp[0][j] - dp[0][k]) for k in range(i, j + 1))
        return dp[-1][-1]

=======
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        def isPossible(maximum: int) -> bool:
            curr = 0
            count = 1
            for num in nums:
                if curr + num > maximum:
                    count += 1
                    curr = num
                else:
                    curr += num
            return count <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(mid: int) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    count += 1
                    total = num
            return count <= k
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 5

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            cuts, curr = 0, 0
            for num in nums:
                curr += num
                if curr > mid:
                    cuts += 1
                    curr = num
            return cuts + 1
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if check(mid) <= k:
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 6

def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(nums, k, target):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > target:
                    count += 1
                    total = num
            return count <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 7

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > mid:
                    count += 1
                    current_sum = num
            return count <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        # dp[i][j] = min(max(dp[i][j], dp[i][j-k], sum(nums[j-k:j])))
        dp = [[float('inf') for _ in range(len(nums)+1)] for _ in range(k+1)]
        dp[0][0] = 0
        for i in range(1, k+1):
            for j in range(1, len(nums)+1):
                for l in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][l], sum(nums[l:j])))
        return dp[k][len(nums)]

=======
Suggestion 9

def splitArray(self, nums: list[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        if k == len(nums):
            return max(nums)
        def isPossible(maxSum):
            count = 1
            currentSum = 0
            for num in nums:
                currentSum += num
                if currentSum > maxSum:
                    currentSum = num
                    count += 1
                    if count > k:
                        return False
            return True
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 10

def splitArray(self, nums: list[int], k: int) -> int:
        def check(m):
            cuts, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum > m:
                    cuts, curr_sum = cuts + 1, num
            return cuts + 1 <= k
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
